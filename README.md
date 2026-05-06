# 🤖 Autonomous Agentic Workflow Manager

> A production-ready autonomous workflow automation system that uses multi-agent AI to execute complex business processes with self-correction capabilities.

**👋 New here? Start with [START_HERE.md](./START_HERE.md)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-blue.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![No API Keys](https://img.shields.io/badge/API%20Keys-Not%20Required-green.svg)](./MODEL_TRAINING.md)

## 🎯 What is This?

Instead of a simple chatbot, this is an **agentic system** that can autonomously execute complex, multi-step business processes like:

- 📋 "Onboard a new client, create their projects in Jira, send a welcome email, and set up billing in Stripe"
- 📄 "Process this invoice, validate the data, create a payment, and send confirmation"
- 🔄 "Sync customer data across systems, update records, and notify stakeholders"

The system uses **multiple AI agents** that work together, validate each other's work, and **self-correct** when errors occur.

## ✨ Key Features

### 🧠 Multi-Agent System (LangGraph)
- **Planner Agent**: Analyzes workflows and creates execution plans
- **Executor Agent**: Executes steps using external tools
- **Validator Agent**: Validates results against expectations
- **Corrector Agent**: Implements self-correction loops

### 🔄 Self-Correction Loops
- Automatic error detection and recovery
- Intelligent retry with corrections
- Validation-driven improvements
- Maximum retry limits to prevent infinite loops

### 🔧 Tool Integration
- **Jira**: Project and issue management
- **Stripe**: Customer and subscription management
- **Email**: Automated notifications
- **Extensible**: Easy to add custom tools

### 🧠 Long-Term Memory
- PostgreSQL-backed memory system
- Agent decision history
- Context retention across sessions
- Memory types: episodic, semantic, procedural

### 🎨 Professional Frontend
- Clean, minimal design (no flashy colors)
- Real-time execution monitoring
- Workflow management interface
- Tool registry viewer

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern async Python web framework
- **LangChain** - LLM orchestration framework
- **LangGraph** - Multi-agent workflow graphs
- **PostgreSQL** - Relational database with JSON support
- **Ollama** - Local LLM inference (100% local, no API keys)
- **SQLAlchemy** - Async ORM

### Frontend
- **React 18** - UI framework with hooks
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling (professional colors)
- **Vite** - Fast build tool
- **Axios** - HTTP client

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Frontend serving

### Local Model Training
- **Jupyter Notebooks** - Interactive training environment
- **PyTorch** - Deep learning framework
- **Transformers** - Model fine-tuning
- **LoRA/PEFT** - Efficient fine-tuning

**🔒 Privacy First**: All models run locally, no API keys required, complete data control

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (React)                      │
│              Clean, Professional Interface               │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/REST
┌────────────────────▼────────────────────────────────────┐
│                  FastAPI Backend                         │
│              Async REST API + WebSockets                 │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              LangGraph Agent System                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Planner  │→ │ Executor │→ │Validator │→ │Corrector│ │
│  │  Agent   │  │  Agent   │  │  Agent   │  │  Agent  │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
│                      ↓                          ↑        │
│                      └──────────────────────────┘        │
│                    (Self-Correction Loop)                │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              Tools & Integrations                        │
│    [Jira]  [Stripe]  [Email]  [Custom APIs]            │
└──────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              PostgreSQL Database                         │
│    Workflows | Executions | Agent Memory | State        │
└──────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd workflow-manager

# 2. Run the quick start script
./quickstart.sh

# 3. Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup

#### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Ollama (for local LLM)

#### Installation Steps

See [SETUP.md](./SETUP.md) for detailed manual setup instructions.

## 💼 Use Cases

### Business Process Automation
- **Client Onboarding**: Create accounts, setup projects, configure billing
- **Employee Onboarding**: Provision accounts, assign tasks, send notifications
- **Invoice Processing**: Extract data, validate, create payments, send confirmations

### Industry-Specific Applications
- **LegalTech**: Document processing, compliance workflows, case management
- **Insurance**: Claims processing, underwriting automation, policy management
- **Healthcare**: Patient onboarding, appointment scheduling, record management
- **Real Estate**: Property management, tenant onboarding, maintenance workflows
- **Finance**: KYC processes, loan origination, fraud detection

### Integration Scenarios
- Multi-system data synchronization
- Automated reporting and notifications
- Cross-platform workflow orchestration
- Event-driven process automation

## 📊 Example: Client Onboarding Workflow

```bash
# Execute the pre-built client onboarding workflow
curl -X POST http://localhost:8000/api/executions \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_id": 1,
    "input_data": {
      "client_name": "Acme Corp",
      "client_email": "contact@acme.com",
      "client_code": "ACME",
      "project_lead_id": "user123",
      "subscription_plan_id": "price_1234"
    }
  }'
```

**What happens:**
1. ✅ Creates Jira project "ACME"
2. ✅ Creates initial setup tasks
3. ✅ Creates Stripe customer
4. ✅ Sets up subscription
5. ✅ Sends welcome email

All with **automatic validation** and **self-correction**!

## 📚 Documentation

**📑 [Complete Documentation Index](./INDEX.md)** - Find everything you need

### Quick Links
- [🚀 Getting Started](./GETTING_STARTED.md) - 5-minute quick start
- [📖 Setup Guide](./SETUP.md) - Detailed installation
- [🏗️ Architecture](./ARCHITECTURE.md) - System design
- [🚀 Deployment](./DEPLOYMENT.md) - Production guide
- [💡 Examples](./EXAMPLES.md) - Usage examples
- [🎯 Features](./FEATURES.md) - Feature breakdown
- [🤝 Contributing](./CONTRIBUTING.md) - How to contribute
- [📋 Project Summary](./PROJECT_SUMMARY.md) - Complete overview

### 🧠 Model Training (No API Keys)
- [📓 Notebooks](./notebooks/) - Jupyter notebooks for local model training
  - `01_model_setup.ipynb` - Set up Ollama and local models
  - `02_model_finetuning.ipynb` - Fine-tune models on workflow tasks
  - `03_workflow_data_collection.ipynb` - Collect training data from executions

**All training runs 100% locally - no external APIs or keys required**

## 🎯 Enterprise-Level Features

- ✅ **Scalability**: Async/await, connection pooling, horizontal scaling
- ✅ **Observability**: Execution tracing, agent decision logging, metrics
- ✅ **Reliability**: Self-correction, retry logic, error recovery
- ✅ **Security**: Credential encryption, input validation, SQL injection prevention
- ✅ **Maintainability**: Clean architecture, type safety, comprehensive docs

## 🌟 Startup Potential

### Why This is Valuable

1. **Privacy-First**: Local LLM means sensitive data never leaves your infrastructure - no API keys required
2. **Cost-Effective**: No per-token API costs, predictable pricing, run unlimited workflows
3. **Autonomous**: Reduces manual intervention with self-correction loops
4. **Extensible**: Easy to add industry-specific tools and workflows
5. **Production-Ready**: Docker-based deployment, comprehensive testing
6. **Trainable**: Fine-tune models on your specific workflows using included notebooks

### Target Markets

- Vertical AI SaaS for underserved industries
- Enterprise workflow automation
- Compliance and regulatory automation
- Multi-system integration platforms

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Ollama](https://ollama.ai/) for local LLM inference
- UI components inspired by modern SaaS design principles

## 📧 Support

- 📖 [Documentation](./README.md)
- 🐛 [Issue Tracker](https://github.com/yourusername/workflow-manager/issues)
- 💬 Community Discord (coming soon)

---

**Autonomous Workflow Automation - Production Ready**
