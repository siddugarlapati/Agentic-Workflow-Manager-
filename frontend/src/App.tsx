import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Workflows from './pages/Workflows'
import Executions from './pages/Executions'
import Tools from './pages/Tools'

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/workflows" element={<Workflows />} />
          <Route path="/executions" element={<Executions />} />
          <Route path="/tools" element={<Tools />} />
        </Routes>
      </Layout>
    </Router>
  )
}

export default App
