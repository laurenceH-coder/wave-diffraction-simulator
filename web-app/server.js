const express = require('express');
const Docker = require('dockerode');
const cors = require('cors');
const net = require('net');
const http = require('http');

const app = express();
const docker = new Docker();

app.use(cors());
app.use(express.json());

const activeSessions = {};
const pendingSessions = {};

const MAX_SESSIONS = 20;                 // hard cap on concurrent containers
const IDLE_TIMEOUT_MS = 20 * 60 * 1000;  // 20 minutes of no heartbeat = idle
const SWEEP_INTERVAL_MS = 5 * 60 * 1000; // check for idle sessions every 5 minutes

const waitForPort = (port, retries = 20, delay = 250) => {
  return new Promise((resolve, reject) => {
    const check = (attemptsLeft) => {
      const socket = new net.Socket();
      socket.on('connect', () => {
        socket.destroy();
        resolve(true);
      });
      socket.on('error', () => {
        socket.destroy();
        if (attemptsLeft <= 0) {
          reject(new Error(`Port ${port} failed to open in time.`));
        } else {
          setTimeout(() => check(attemptsLeft - 1), delay);
        }
      });
      socket.connect(port, '127.0.0.1');
    };
    check(retries);
  });
};

// Confirms the web app is actually serving real content, not just that the port is open
const waitForHttpReady = (port, retries = 30, delay = 500) => {
  return new Promise((resolve, reject) => {
    const check = (attemptsLeft) => {
      const req = http.get(
        { host: '127.0.0.1', port, path: '/index.html', timeout: 2000 },
        (res) => {
          res.resume();
          if (res.statusCode === 200) {
            resolve(true);
          } else {
            retry(attemptsLeft);
          }
        }
      );
      req.on('error', () => retry(attemptsLeft));
      req.on('timeout', () => {
        req.destroy();
        retry(attemptsLeft);
      });
    };

    const retry = (attemptsLeft) => {
      if (attemptsLeft <= 0) {
        reject(new Error(`App on port ${port} never became ready.`));
      } else {
        setTimeout(() => check(attemptsLeft - 1), delay);
      }
    };

    check(retries);
  });
};

// Removes a container by ID, swallowing errors (e.g. already gone)
const safeRemoveContainer = async (containerId, label) => {
  try {
    const container = docker.getContainer(containerId);
    await container.remove({ force: true });
    console.log(`Removed container ${label}`);
  } catch (err) {
    console.error(`Failed to remove container ${label}:`, err.message);
  }
};

// On startup, clean up any containers left over from a previous crashed/killed run
const cleanupOrphans = async () => {
  try {
    const containers = await docker.listContainers({
      all: true,
      filters: { name: ['wave-sim-'] },
    });
    for (const c of containers) {
      await safeRemoveContainer(c.Id, c.Names[0]);
    }
    if (containers.length > 0) {
      console.log(`Cleaned up ${containers.length} orphaned container(s) from a previous run.`);
    }
  } catch (err) {
    console.error('Orphan cleanup failed:', err.message);
  }
};

// Periodic sweep: remove sessions that haven't sent a heartbeat recently
const startIdleSweep = () => {
  setInterval(async () => {
    const now = Date.now();
    for (const sessionId of Object.keys(activeSessions)) {
      const session = activeSessions[sessionId];
      if (now - session.lastActive > IDLE_TIMEOUT_MS) {
        console.log(`Session ${sessionId} idle for too long, cleaning up.`);
        await safeRemoveContainer(session.containerId, `wave-sim-${sessionId}`);
        delete activeSessions[sessionId];
      }
    }
  }, SWEEP_INTERVAL_MS);
};

app.post('/api/start-session', async (req, res) => {
  const { sessionId } = req.body;

  if (activeSessions[sessionId]) {
    activeSessions[sessionId].lastActive = Date.now();
    const existingUrl = `http://127.0.0.1:${activeSessions[sessionId].port}/index.html?autoconnect=true&resize=scale&t=${Date.now()}`;
    return res.json({ url: existingUrl });
  }

  if (pendingSessions[sessionId]) {
    try {
      const url = await pendingSessions[sessionId];
      return res.json({ url });
    } catch (err) {
      return res.status(500).json({ error: 'Container failed to initialize.' });
    }
  }

  if (Object.keys(activeSessions).length >= MAX_SESSIONS) {
    return res.status(503).json({ error: 'Server is at capacity, please try again shortly.' });
  }

  const containerName = `wave-sim-${sessionId}`;

  const creationPromise = (async () => {
    try {
      const stale = docker.getContainer(containerName);
      await stale.remove({ force: true });
      console.log(`Removed stale container ${containerName}`);
    } catch (cleanupErr) {
      // fine, no stale container existed
    }

    const container = await docker.createContainer({
      Image: 'wave-simulator:latest',
      name: containerName,
      ExposedPorts: { '8080/tcp': {} },
      HostConfig: {
        PortBindings: {
          '8080/tcp': [{ HostIp: '127.0.0.1', HostPort: '' }],
        },
        Memory: 512 * 1024 * 1024, // 512MB cap per container
        NanoCpus: 1_000_000_000,   // 1 CPU core cap per container
      },
    });

    await container.start();

    const info = await container.inspect();
    const assignedPort = info.NetworkSettings.Ports['8080/tcp'][0].HostPort;

    await waitForPort(assignedPort);
    console.log(`Port ${assignedPort} open, waiting for app to be fully ready...`);
    await waitForHttpReady(assignedPort);
    console.log(`App on port ${assignedPort} confirmed ready.`);

    activeSessions[sessionId] = {
      containerId: container.id,
      port: assignedPort,
      lastActive: Date.now(),
    };

    return `http://127.0.0.1:${assignedPort}/index.html?autoconnect=true&resize=scale&t=${Date.now()}`;
  })();

  pendingSessions[sessionId] = creationPromise;

  try {
    const url = await creationPromise;
    res.json({ url });
  } catch (err) {
    console.error('Failed to start container session:', err.message);
    res.status(500).json({ error: 'Container failed to initialize.' });
  } finally {
    delete pendingSessions[sessionId];
  }
});

// Lightweight endpoint the frontend pings periodically to prove the user is still active,
// so the idle sweep doesn't kill a session someone is genuinely using.
app.post('/api/heartbeat', (req, res) => {
  const { sessionId } = req.body;
  if (activeSessions[sessionId]) {
    activeSessions[sessionId].lastActive = Date.now();
    return res.json({ ok: true });
  }
  res.status(404).json({ ok: false, error: 'Session not found.' });
});

// Graceful shutdown: tear down whatever containers this process created
const shutdown = async () => {
  console.log('Shutting down, cleaning up containers...');
  for (const sessionId of Object.keys(activeSessions)) {
    await safeRemoveContainer(activeSessions[sessionId].containerId, `wave-sim-${sessionId}`);
  }
  process.exit(0);
};
process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);

cleanupOrphans().then(() => {
  startIdleSweep();
  app.listen(5000, () => console.log('Orchestrator running on http://127.0.0.1:5000'));
});