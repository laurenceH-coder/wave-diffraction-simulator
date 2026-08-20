# Wave Diffraction Simulator

An interactive desktop physics simulator that visualises how light diffracts through single- and double-slit gratings — built with Python/Tkinter and shipped to the browser via a Dockerized noVNC session, orchestrated per-user by a Node/Express backend.

![Intensity profile example](Wave%20Diffraction%20Simulator/assets/IntensityProfilePeakHigh.png)

## What it does

The simulator lets a user build a diffraction setup and see the resulting interference pattern update live:

- **Grating types** — single slit, double slit, and multi-slit diffraction gratings, with adjustable slit width/spacing
- **Wavelength control** — a slider across the visible spectrum (380–700 nm) that recolours the simulated beam and pattern in real time
- **Measurement tools** — an on-screen ruler and protractor for measuring fringe spacing and diffraction angle directly on the canvas
- **Intensity profile** — a live graph of the diffraction pattern's intensity distribution alongside the visual pattern
- **Screen distance control** — adjust the grating-to-screen distance and watch the pattern scale accordingly
- **Save/load setups** — store up to three configurations in-session and reload them from the main menu

## Why it's built this way

Tkinter doesn't run in a browser, so to make the simulator shareable as a link rather than a download, the project wraps the desktop app in a headless X server (Xvfb) + noVNC, containerises that with Docker, and fronts it with a small orchestrator that:

- spins up an isolated, resource-capped container per visitor session (`server.js`, using [dockerode](https://github.com/apocas/dockerode))
- waits for the app inside to actually be ready (not just "port open") before handing back a URL
- keeps sessions alive via a heartbeat from the client, and sweeps/removes idle containers automatically
- caps concurrent sessions so the host doesn't fall over under load

The React app (`my-react-app/`) then embeds that per-session simulator in an iframe.

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
| Simulation engine / GUI | Python, Tkinter, Pillow, NumPy, colorpy |
| Browser delivery | Xvfb, x11vnc, noVNC, websockify (Docker) |
| Session orchestration | Node.js, Express, Dockerode |
| Frontend | React |

## Running it

### Option A — native desktop app (simplest, for trying the physics)

```bash
cd "Wave Diffraction Simulator"
pip install -r requirements.txt
python3 WaveDiffractionSimulator.py
```

Requires Python 3 with Tkinter available (bundled on Windows/macOS installers; on Linux install `python3-tk`).

### Option B — full browser stack (simulator container + orchestrator + web UI)

```bash
# 1. Build the simulator image
cd "Wave Diffraction Simulator"
docker build -t wave-simulator:latest .

# 2. Start the orchestrator (needs Docker socket access)
cd ../my-react-app
npm install
node server.js

# 3. Start the frontend
npm start
```

The orchestrator listens on `:5000` and provisions containers on demand; the React app talks to it via `REACT_APP_ORCHESTRATOR_URL`.

## Project structure

```
Wave Diffraction Simulator/   # Python/Tkinter simulator, Dockerfile, noVNC entrypoint
my-react-app/                 # React frontend + Express/Dockerode session orchestrator
```

## Status & known limitations

- Session state (save slots) is in-memory per container and is lost when a session is cleaned up — this is by design for a stateless demo, not a bug.
- The orchestrator binds containers to `127.0.0.1`, so as-is it's intended to sit behind a reverse proxy rather than be exposed directly.
- Built as a personal/portfolio project rather than a production service — see the `assets/old scripts (ignore)/` folder for earlier iterations kept for reference.

## License

MIT — see [LICENSE](LICENSE).
