import { useEffect, useState } from 'react'
import { Wrench } from 'lucide-react'
import { api } from '../services/api'

export default function Tools() {
  const [tools, setTools] = useState([])
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    loadTools()
  }, [])
  
  const loadTools = async () => {
    try {
      const data = await api.getTools()
      setTools(data.tools || [])
    } catch (error) {
      console.error('Failed to load tools:', error)
    } finally {
      setLoading(false)
    }
  }
  
  if (loading) {
    return <div className="text-center py-12">Loading...</div>
  }
  
  return (
    <div className="px-4 py-6 sm:px-0">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">Available Tools</h2>
      
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {tools.map((tool: any) => (
          <div key={tool.name} className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <Wrench className="h-6 w-6 text-primary-600" />
                </div>
                <div className="ml-5 w-0 flex-1">
                  <h3 className="text-lg font-medium text-gray-900">
                    {tool.name}
                  </h3>
                  <p className="mt-1 text-sm text-gray-500">
                    {tool.description}
                  </p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
