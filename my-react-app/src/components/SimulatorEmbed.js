import React, { useEffect, useState, useRef } from 'react';

const ORCHESTRATOR_URL = process.env.REACT_APP_ORCHESTRATOR_URL || 'http://localhost:5000';
const HEARTBEAT_INTERVAL_MS = 5 * 60 * 1000; // ping every 5 minutes while the tab is open

const SimulatorEmbed = () => {
  const [simulatorUrl, setSimulatorUrl] = useState(null);
  const [loading, setLoading] = useState(true);
  const iframeRef = useRef(null);
  const sessionIdRef = useRef(null);

  useEffect(() => {
    let sessionId = sessionStorage.getItem('wave_sim_session_id');
    if (!sessionId) {
      sessionId = 'session_' + Math.random().toString(36).substring(2, 9);
      sessionStorage.setItem('wave_sim_session_id', sessionId);
    }
    sessionIdRef.current = sessionId;

    fetch(`${ORCHESTRATOR_URL}/api/start-session`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-cache' },
      body: JSON.stringify({ sessionId }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.url) {
          setSimulatorUrl(data.url);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to connect to orchestrator backend:', err);
        setLoading(false);
      });
  }, []);

  // Keep the server-side session alive while this tab is genuinely open
  useEffect(() => {
    if (!simulatorUrl) return;

    const sendHeartbeat = () => {
      fetch(`${ORCHESTRATOR_URL}/api/heartbeat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sessionId: sessionIdRef.current }),
      }).catch(() => {
        // Non-fatal — a missed heartbeat just means the idle sweep may
        // eventually clean this session up, which is the correct fallback.
      });
    };

    const interval = setInterval(sendHeartbeat, HEARTBEAT_INTERVAL_MS);
    return () => clearInterval(interval);
  }, [simulatorUrl]);

  const handleIframeLoad = () => {
    if (iframeRef.current) {
      iframeRef.current.focus();
    }
  };

  if (loading) {
    return (
      <div style={styles.loadingBox}>
        <p>Launching your isolated Wave Simulator environment...</p>
      </div>
    );
  }

  if (!simulatorUrl) {
    return (
      <div style={styles.loadingBox}>
        <p>Unable to connect to the simulator server. Please try again.</p>
      </div>
    );
  }

  return (
    <div style={styles.outerWrapper} onClick={() => iframeRef.current?.focus()}>
      <iframe
        key={simulatorUrl}
        ref={iframeRef}
        src={simulatorUrl}
        title="Wave Diffraction Simulator"
        style={styles.iframe}
        onLoad={handleIframeLoad}
        allow="autoplay; fullscreen"
        tabIndex="0"
      />
    </div>
  );
};

const styles = {
  loadingBox: {
    width: '100%',
    maxWidth: '1280px',
    height: '500px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    color: '#fff',
    backgroundColor: '#111',
    borderRadius: '8px',
  },
  outerWrapper: {
    width: '100%',
    maxWidth: '1280px',
    height: 'calc(100vh - 120px)',
    maxHeight: '800px',
    backgroundColor: '#000',
    borderRadius: '8px',
    overflow: 'hidden',
    boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
  },
  iframe: {
    width: '100%',
    height: '100%',
    border: 'none',
    display: 'block',
  },
};

export default SimulatorEmbed;