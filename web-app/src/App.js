import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import SimulatorEmbed from './components/SimulatorEmbed';

function App() {
  const SIMULATOR_URL = process.env.REACT_APP_SIMULATOR_URL || 'http://localhost:8080';

  return (
    <div style={styles.appContainer}>
      <Header />
      <main style={styles.mainContent}>
        <SimulatorEmbed simulatorUrl={SIMULATOR_URL} />
      </main>
      <Footer />
    </div>
  );
}

const styles = {
  appContainer: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    backgroundColor: '#1a1a1a',
  },
  mainContent: {
    flex: 1,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '20px',
  },
};

export default App;