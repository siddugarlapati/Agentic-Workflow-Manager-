import { useEffect, useState } from 'react'
import { Activity, CheckCircle, XCircle, Clock } from 'lucide-react'
import { api } from '../services/api'

export default function Dashboard() {
  const [stats, setStats] = useState({
    total: 0,
    running: 0,
    completed: 0,
    failed: 0
  })
  
  useEffect(() => {
    loadStats()
  }, [])
  
  const loadStats = async () => {
    try {
      const executions = await api.getExecutions()
      setStats({
        total: executions.length,
        running: executions.filter((e: any) => e.status === 'running').length,
        completed: executions.filter((e: any) => e.status === 'completed').length,
        failed: executions.filter((e: any) => e.status === 'failed').length
      })
    } catch (error) {
      console.error('Failed to load stats:', error)
    }
  }
  
  const statCards = [
    { label: 'Total Executions', value: stats.total, icon: Activity, color: 'blue' },
    { label: 'Running', value: stats.running, icon: Clock, color: 'yellow' },
    { label: 'Completed', value: stats.completed, icon: CheckCircle, color: 'green' },
    { label: 'Failed', value: stats.failed, icon: XCircle, color: 'red' }
  ]
  
  return (
    <div className="px-4 py-6 sm:px-0">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">Dashboard</h2>
      
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        {statCards.map((stat) => {
          const Icon = stat.icon
          return (
            <div key={stat.label} className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <Icon className={`h-6 w-6 text-${stat.color}-600`} />
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">
                        {stat.label}
                      </dt>
                      <dd className="text-2xl font-semibold text-gray-900">
                        {stat.value}
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
