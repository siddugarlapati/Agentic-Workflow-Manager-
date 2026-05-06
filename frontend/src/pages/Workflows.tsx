import { useEffect, useState } from 'react'
import { Plus, Play } from 'lucide-react'
import { api } from '../services/api'

export default function Workflows() {
  const [workflows, setWorkflows] = useState([])
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    loadWorkflows()
  }, [])
  
  const loadWorkflows = async () => {
    try {
      const data = await api.getWorkflows()
      setWorkflows(data)
    } catch (error) {
      console.error('Failed to load workflows:', error)
    } finally {
      setLoading(false)
    }
  }
  
  const handleExecute = async (workflowId: number) => {
    try {
      await api.startExecution(workflowId, {})
      alert('Workflow execution started!')
    } catch (error) {
      console.error('Failed to start execution:', error)
    }
  }
  
  if (loading) {
    return <div className="text-center py-12">Loading...</div>
  }
  
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-semibold text-gray-800">Workflows</h2>
        <button className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700">
          <Plus className="w-4 h-4 mr-2" />
          New Workflow
        </button>
      </div>
      
      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {workflows.map((workflow: any) => (
            <li key={workflow.id}>
              <div className="px-4 py-4 flex items-center sm:px-6">
                <div className="min-w-0 flex-1">
                  <h3 className="text-lg font-medium text-gray-900">
                    {workflow.name}
                  </h3>
                  <p className="mt-1 text-sm text-gray-500">
                    {workflow.description}
                  </p>
                </div>
                <div className="ml-5 flex-shrink-0">
                  <button
                    onClick={() => handleExecute(workflow.id)}
                    className="inline-flex items-center px-3 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                  >
                    <Play className="w-4 h-4 mr-2" />
                    Execute
                  </button>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}
