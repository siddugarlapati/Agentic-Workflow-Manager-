import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const api = {
  // Workflows
  getWorkflows: async () => {
    const response = await apiClient.get('/workflows')
    return response.data
  },
  
  getWorkflow: async (id: number) => {
    const response = await apiClient.get(`/workflows/${id}`)
    return response.data
  },
  
  createWorkflow: async (workflow: any) => {
    const response = await apiClient.post('/workflows', workflow)
    return response.data
  },
  
  // Executions
  getExecutions: async () => {
    const response = await apiClient.get('/executions')
    return response.data
  },
  
  getExecution: async (id: number) => {
    const response = await apiClient.get(`/executions/${id}`)
    return response.data
  },
  
  startExecution: async (workflowId: number, inputData: any) => {
    const response = await apiClient.post('/executions', {
      workflow_id: workflowId,
      input_data: inputData
    })
    return response.data
  },
  
  // Tools
  getTools: async () => {
    const response = await apiClient.get('/tools')
    return response.data
  }
}
