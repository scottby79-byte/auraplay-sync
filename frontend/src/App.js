import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import DashboardPage from './pages/DashboardPage';
import TransferPage from './pages/TransferPage';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/transfer/:profileId" element={<TransferPage />} />
          {/* Add other routes here as the application grows */}
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;

