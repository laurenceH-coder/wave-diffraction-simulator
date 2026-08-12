#!/bin/bash

touch /root/.Xauthority
export DISPLAY=:99
export XAUTHORITY=/root/.Xauthority

# Start Xvfb virtual display
Xvfb :99 -screen 0 1920x1080x24 &
sleep 2

# Start Fluxbox
fluxbox &
sleep 1

# Start x11vnc
x11vnc -display :99 -forever -shared -noxfixes -nopw -rfbport 5900 &
sleep 2

# Start Python wave application
python3 /app/WaveDiffractionSimulator.py &
sleep 1

# Bind websockify to 0.0.0.0:8080 explicitly
websockify --web /usr/share/novnc 0.0.0.0:8080 127.0.0.1:5900