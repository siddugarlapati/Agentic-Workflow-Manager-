# 📚 Documentation Index

Welcome to the Autonomous Agentic Workflow Manager documentation! This index will help you find what you need.

## 🚀 Getting Started

**New to the project?** Start here:

1. **[README.md](./README.md)** - Project overview and introduction
2. **[GETTING_STARTED.md](./GETTING_STARTED.md)** - Quick start guide (5 minutes)
3. **[SETUP.md](./SETUP.md)** - Detailed installation instructions

## 📖 Core Documentation

### Understanding the System

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design and architecture
  - Multi-agent system design
  - Component interactions
  - Technology choices
  - Scalability considerations

- **[FEATURES.md](./FEATURES.md)** - Complete feature breakdown
  - Core features
  - Agent capabilities
  - Tool integrations
  - UI features
  - Security features

- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Comprehensive project overview
  - Key features
  - Tech stack
  - Project structure
  - Enterprise-level features
  - Startup potential

- **[PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)** - High-level project summary
  - What we built
  - Statistics
  - Achievements
  - Use cases
  - Next steps

## 💻 Development

### For Developers

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute
  - Development setup
  - Code style
  - Testing
  - Pull request guidelines

- **[EXAMPLES.md](./EXAMPLES.md)** - Usage examples and tutorials
  - Client onboarding workflow
  - Invoice processing
  - Custom workflows
  - Adding custom tools
  - Testing

### Code Structure

```
backend/
├── app/
│   ├── agents/          # AI agents (Planner, Executor, Validator, Corrector)
│   ├── api/             # REST API endpoints
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   ├── tools/           # Tool integrations
│   └── templates/       # Workflow templates

frontend/
├── src/
│   ├── components/      # React components
│   ├── pages/           # Page components
│   └── services/        # API client
```

## 🚀 Deployment

### Production Deployment

- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Production deployment guide
  - Docker Compose deployment
  - Kubernetes deployment
  - Cloud deployment (AWS, GCP)
  - Environment variables
  - Performance tuning
  - Monitoring
  - Backup strategy
  - Security checklist

### Quick Deploy

```bash
# Quick start
./quickstart.sh

# Docker Compose
docker-compose up -d

# Access
Frontend: http://localhost:5173
API: http://localhost:8000
Docs: http://localhost:8000/docs
```

## 📚 Reference

### API Documentation

- **Interactive API Docs**: http://localhost:8000/docs (when running)
- **OpenAPI Spec**: http://localhost:8000/openapi.json

### Workflow Templates

- **Client Onboarding**: `backend/app/templates/client_onboarding.json`
- More templates coming soon!

### Tool Reference

Built-in tools:
- **Jira**: Project and issue management
- **Stripe**: Payment processing
- **Email**: Automated notifications

See [EXAMPLES.md](./EXAMPLES.md) for adding custom tools.

## 🎯 Use Cases

### By Industry

**LegalTech**
- Document processing
- Compliance workflows
- Case management

**Insurance**
- Claims processing
- Underwriting automation
- Policy management

**Healthcare**
- Patient onboarding
- Appointment scheduling
- Record management

**Real Estate**
- Property management
- Tenant onboarding
- Maintenance workflows

**Finance**
- KYC processes
- Loan origination
- Fraud detection

### By Function

**Client Management**
- Onboarding automation
- Account setup
- Billing configuration

**Project Management**
- Project creation
- Task assignment
- Status tracking

**Communication**
- Email automation
- Notification systems
- Multi-channel messaging

## 🔧 Configuration

### Environment Setup

```env
# Database
DATABASE_URL=postgresql://localhost/workflow_manager

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1

# Integrations
JIRA_URL=https://your-domain.atlassian.net
STRIPE_API_KEY=sk_test_your_key
SMTP_HOST=smtp.gmail.com
```

See [SETUP.md](./SETUP.md) for complete configuration.

## 🐛 Troubleshooting

### Common Issues

**Services not starting**
```bash
docker-compose logs
docker-compose restart
```

**Database connection issues**
```bash
docker-compose restart postgres
```

**Ollama model not loading**
```bash
docker exec -it workflow-manager-ollama-1 ollama pull llama3.1
```

See [GETTING_STARTED.md](./GETTING_STARTED.md) for more troubleshooting.

## 📊 Project Statistics

- **44** Source files
- **12** Documentation files
- **4** AI Agents
- **5** Built-in tools
- **4** Frontend pages
- **100%** Async implementation
- **Full** Docker support

## 🎓 Learning Path

### Beginner
1. Read [README.md](./README.md)
2. Follow [GETTING_STARTED.md](./GETTING_STARTED.md)
3. Try [EXAMPLES.md](./EXAMPLES.md)

### Intermediate
1. Study [ARCHITECTURE.md](./ARCHITECTURE.md)
2. Review [FEATURES.md](./FEATURES.md)
3. Explore the codebase

### Advanced
1. Read [DEPLOYMENT.md](./DEPLOYMENT.md)
2. Contribute via [CONTRIBUTING.md](./CONTRIBUTING.md)
3. Build custom tools and agents

## 🔗 Quick Links

### Documentation
- [README](./README.md) - Main documentation
- [Getting Started](./GETTING_STARTED.md) - Quick start
- [Setup](./SETUP.md) - Installation
- [Architecture](./ARCHITECTURE.md) - System design
- [Features](./FEATURES.md) - Feature list
- [Examples](./EXAMPLES.md) - Usage examples
- [Deployment](./DEPLOYMENT.md) - Production guide
- [Contributing](./CONTRIBUTING.md) - Contribution guide

### Project Info
- [Project Summary](./PROJECT_SUMMARY.md) - Complete overview
- [Project Overview](./PROJECT_OVERVIEW.md) - High-level summary
- [License](./LICENSE) - MIT License

### Resources
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173
- GitHub: (add your repo URL)

## 🆘 Support

### Getting Help

1. **Documentation**: Read the relevant .md file
2. **API Docs**: Check http://localhost:8000/docs
3. **Logs**: Run `docker-compose logs`
4. **Issues**: GitHub issue tracker
5. **Discussions**: GitHub discussions

### Contact

- 📧 Email: support@example.com (update this)
- 💬 Discord: (coming soon)
- 🐦 Twitter: (add your handle)

## 🎯 Next Steps

**Just starting?**
→ [GETTING_STARTED.md](./GETTING_STARTED.md)

**Want to understand the system?**
→ [ARCHITECTURE.md](./ARCHITECTURE.md)

**Ready to deploy?**
→ [DEPLOYMENT.md](./DEPLOYMENT.md)

**Want to contribute?**
→ [CONTRIBUTING.md](./CONTRIBUTING.md)

**Need examples?**
→ [EXAMPLES.md](./EXAMPLES.md)

---

**Autonomous Workflow Automation - Production Ready**
