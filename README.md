# Wave Diffraction Simulator

An interactive desktop physics simulator that shows how light diffracts through single and double slits. It is written in Python with Tkinter, and to make it easy to share it also runs in the browser. A Docker container serves the app through noVNC, and a Node/Express backend starts a separate container for each visitor.

![Intensity profile example](simulator/assets/IntensityProfilePeakHigh.png)

## What it does

You build a diffraction setup and watch the interference pattern update live.

- **Grating types:** single slit, double slit and multi-slit gratings, with adjustable slit width and spacing.
- **Wavelength control:** a slider across the visible spectrum (380 to 700 nm) that recolours the beam and the pattern in real time.
- **Measurement tools:** an on-screen ruler and protractor for measuring fringe spacing and diffraction angle directly on the canvas.
- **Intensity profile:** a live graph of the pattern's intensity next to the visual pattern.
- **Screen distance:** change the distance from the grating to the screen and watch the pattern scale.
- **Save and load:** keep up to three setups per session and reload them from the main menu.

## Why it is built this way

Tkinter apps do not run in a browser. I wanted people to be able to open the simulator from a link instead of installing it, so the app runs inside a Docker container with a headless X server (Xvfb) and noVNC. A small orchestrator sits in front of it and:

- starts an isolated, resource-capped container for each visitor session (`server.js`, using [dockerode](https://github.com/apocas/dockerode))
- waits until the app inside is actually ready, not just listening on a port, before returning a URL
- keeps sessions alive with a heartbeat from the client, and removes idle containers automatically
- limits the number of concurrent sessions so the host is not overloaded

The React app in `web-app/` embeds each session's simulator in an iframe.

```
Browser (React) ──POST /api/start-session──▶ Express/Dockerode orchestrator
                                                        │
                                              docker run wave-simulator
                                                        │
                                    Xvfb + Tkinter app + x11vnc + noVNC (port 8080)
                                                        │
Browser (React) ◀── iframe: http://host:<port>/index.html ──┘
```

## Tech stack

| Layer | Tools |
|---|---|
| Simulation engine and GUI | Python, Tkinter, Pillow, NumPy, colorpy |
| Browser delivery | Xvfb, x11vnc, noVNC, websockify (Docker) |
| Session orchestration | Node.js, Express, Dockerode |
| Frontend | React |

## Running it

### Option A: native desktop app

This is the simplest way to try the physics.

```bash
cd simulator
pip install -r requirements.txt
python3 WaveDiffractionSimulator.py
```

You need Python 3 with Tkinter. It comes with the Windows and macOS installers, and on Linux you can install it with `python3-tk`.

### Option B: full browser stack

This runs the simulator container, the orchestrator and the web UI together.

```bash
# 1. Build the simulator image
cd simulator
docker build -t wave-simulator:latest .

# 2. Start the orchestrator (needs access to the Docker socket)
cd ../web-app
npm install
node server.js

# 3. Start the frontend
npm start
```

The orchestrator listens on port 5000 and starts containers on demand. The React app finds it through `REACT_APP_ORCHESTRATOR_URL`.

## Project structure

```
simulator/   # Python/Tkinter simulator, Dockerfile, noVNC entrypoint
web-app/     # React frontend and the Express/Dockerode session orchestrator
```

## Status and known limitations

- Save slots are held in memory inside each container, so they are lost when a session is cleaned up. This is deliberate for a stateless demo, not a bug.
- The orchestrator binds containers to `127.0.0.1`, so it is meant to sit behind a reverse proxy and not be exposed directly.
- This is a personal project, not a production service. Earlier iterations of the code are kept in `simulator/assets/old scripts (ignore)/` for reference.

## Licence

MIT. See [LICENSE](LICENSE).
