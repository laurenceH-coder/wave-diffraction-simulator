FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    xvfb \
    x11vnc \
    xauth \
    novnc \
    websockify \
    fluxbox \
    dos2unix \
    xclip \
    netcat \
    && rm -rf /var/lib/apt-get/lists/*

WORKDIR /app

# Copy default vnc.html to index.html
RUN cp /usr/share/novnc/vnc.html /usr/share/novnc/index.html

# 1. Hide control bar and force aspect-fit canvas scaling via CSS
RUN sed -i 's|</head>|<style>#noVNC_control_bar, .noVNC_control_bar { display: none !important; } html, body { margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden !important; background-color: #000; display: flex; justify-content: center; align-items: center; }</style></head>|' /usr/share/novnc/index.html

# 2. Force downscale in noVNC UI script defaults
RUN sed -i 's|UI.initSetting("resize", "off");|UI.initSetting("resize", "scale");|g' /usr/share/novnc/app/ui.js || true

# 3. Add global listener to capture pointer focus inside the iframe
RUN sed -i 's|</body>|<script>window.addEventListener("load", function(){ window.addEventListener("pointerdown", function(){ var c = document.querySelector("canvas"); if(c) c.focus(); }); });</script></body>|' /usr/share/novnc/index.html

# Copy project files
COPY . /app/

# Install python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Fix line endings
RUN dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh

EXPOSE 6080
EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]