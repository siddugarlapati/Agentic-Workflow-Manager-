import { useEffect, useState } from 'react'
import { format } from 'date-fns'
import { api } from '../services/api'

const statusColors: Record<string, string> = {
  pending: 'bg-gray-100 text-gray-800',
  running: 'bg-yellow-100 text-yellow-800',
  completed: 'bg-green-100 text-green-800',
  failed: 'bg-red-100 text-red-800'
}

export default function Executions() {
  const [executions, setExecutions] = useState([])
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    loadExecutions()
    const interval = setInterval(loadExecutions, 5000) // Refresh every 5s
    return () => clearInterval(interval)
  }, [])
  
  const loadExecutions = async () => {
    try {
      const data = await api.getExecutions()
      setExecutions(data)
    } catch (error) {
      console.error('Failed to load executions:', error)
    } finally {
      setLoading(false)
    }
  }
  
  if (loading) {
    return <div className="text-center py-12">Loading...</div>
  }
  
  return (
    <div className="px-4 py-6 sm:px-0">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">Executions</h2>
      
      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {executions.map((execution: any) => (
            <li key={execution.id}>
              <div className="px-4 py-4 sm:px-6">
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <p className="text-sm font-medium text-gray-900">
                      Execution #{execution.id}
                    </p>
                    <p className="text-sm text-gray-500">
                      Started: {execution.started_at ? format(new Date(execution.started_at), 'PPpp') : 'N/A'}
                    </p>
                  </div>
                  <div>
                    <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${statusColors[execution.status]}`}>
                      {execution.status}
                    </span>
                  </div>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}
