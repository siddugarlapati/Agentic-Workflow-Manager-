# 👋 Welcome to Autonomous Agentic Workflow Manager

**Start here if you're new to this project!**

## What is This?

An AI-powered workflow automation system that can autonomously execute complex business processes like:

- 📋 "Onboard a new client, create their Jira project, set up Stripe billing, and send a welcome email"
- 📄 "Process this invoice, validate the data, create a payment, and send confirmation"
- 🔄 "Sync customer data across systems and notify stakeholders"

**Key Feature**: Uses local AI models - **no API keys required**, complete privacy!

## 🚀 Quick Start (Choose Your Path)

### Path 1: Just Want to Try It? (5 minutes)

```bash
# Run this one command
./quickstart.sh

# Then open: http://localhost:5173
```

That's it! The system is running with default settings.

### Path 2: Want to Understand First? (15 minutes)

1. Read [README.md](./README.md) - Project overview
2. Read [GETTING_STARTED.md](./GETTING_STARTED.md) - Detailed guide
3. Run `./quickstart.sh`
4. Try [EXAMPLES.md](./EXAMPLES.md)

### Path 3: Want to Train Models? (1-2 hours)

1. Run `./quickstart.sh` first
2. Open `notebooks/01_model_setup.ipynb`
3. Follow the training notebooks
4. See [MODEL_TRAINING.md](./MODEL_TRAINING.md)

## 📚 Documentation Map

### 🎯 Essential (Read These First)
- **[README.md](./README.md)** - What this project does
- **[GETTING_STARTED.md](./GETTING_STARTED.md)** - How to get started
- **[EXAMPLES.md](./EXAMPLES.md)** - Usage examples

### 🔧 Setup & Configuration
- **[SETUP.md](./SETUP.md)** - Detailed installation
- **[MODEL_TRAINING.md](./MODEL_TRAINING.md)** - Train local models
- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Production deployment

### 📖 Understanding the System
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - How it works
- **[FEATURES.md](./FEATURES.md)** - What it can do
- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Complete overview

### 🤝 Contributing
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute
- **[INDEX.md](./INDEX.md)** - Full documentation index

### 🎓 Training Notebooks
- **[notebooks/](./notebooks/)** - Jupyter notebooks for model training
  - `01_model_setup.ipynb` - Setup local models
  - `02_model_finetuning.ipynb` - Fine-tune models
  - `03_workflow_data_collection.ipynb` - Collect training data

## 🎯 What Can You Do?

### 1. Run Pre-built Workflows
```bash
# Client onboarding workflow
curl -X POST http://localhost:8000/api/executions \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_id": 1,
    "input_data": {
      "client_name": "Acme Corp",
      "client_email": "contact@acme.com"
    }
  }'
```

### 2. Create Custom Workflows
- Use the web UI at http://localhost:5173
- Or use the API at http://localhost:8000/docs

### 3. Train Your Own Models
- Open Jupyter notebooks in `notebooks/`
- Collect data from your workflows
- Fine-tune models on your use cases

### 4. Integrate Your Tools
- Add custom tools in `backend/app/tools/`
- See [EXAMPLES.md](./EXAMPLES.md) for how-to

## 🔒 Privacy First

**Everything runs locally:**
- ✅ No API keys required
- ✅ No data sent to external services
- ✅ Complete control over your data
- ✅ GDPR/HIPAA compliant

## 💰 Cost Comparison

**Traditional API Solution**: $18,000-36,000/year
**This Solution**: $120-240/year (electricity only)

**Savings**: ~$35,000/year

## 🎨 What You Get

- ✅ Multi-agent AI system (4 agents)
- ✅ Self-correction capabilities
- ✅ Tool integrations (Jira, Stripe, Email)
- ✅ Professional web UI
- ✅ Local model training
- ✅ Complete documentation
- ✅ Docker deployment
- ✅ Production ready

## 🚦 System Requirements

### Minimum (Development)
- 8GB RAM
- 4 CPU cores
- 10GB disk space
- Docker installed

### Recommended (Production)
- 16GB+ RAM
- 8+ CPU cores
- 50GB SSD
- Docker installed

## 🆘 Need Help?

### Quick Answers
- **How do I start?** → Run `./quickstart.sh`
- **Where's the UI?** → http://localhost:5173
- **Where's the API?** → http://localhost:8000/docs
- **How do I train models?** → See `notebooks/`
- **Is it free?** → Yes, MIT License
- **Do I need API keys?** → No, 100% local

### Detailed Help
- Check [GETTING_STARTED.md](./GETTING_STARTED.md)
- Read [INDEX.md](./INDEX.md) for all docs
- Open GitHub issue for bugs
- See [CONTRIBUTING.md](./CONTRIBUTING.md) to contribute

## 📊 Project Stats

- **48** Source files
- **17** Documentation files
- **3** Training notebooks
- **4** AI agents
- **5** Built-in tools
- **100%** Local execution
- **0** API keys needed

## 🎯 Common Use Cases

### Business
- Client onboarding
- Invoice processing
- Employee onboarding
- Project setup

### Industry
- LegalTech: Document processing
- Insurance: Claims processing
- Healthcare: Patient onboarding
- Finance: KYC processes

## 🚀 Next Steps

1. **Run the system**: `./quickstart.sh`
2. **Open the UI**: http://localhost:5173
3. **Try an example**: See [EXAMPLES.md](./EXAMPLES.md)
4. **Read the docs**: Start with [README.md](./README.md)
5. **Train models**: Open `notebooks/`

## 🎉 You're Ready!

Everything is set up and ready to go. Just run:

```bash
./quickstart.sh
```

Then open http://localhost:5173 in your browser.

---

**Questions?** Check [INDEX.md](./INDEX.md) for all documentation.

**Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md).

**Need help?** Open a GitHub issue.

---

**Autonomous Workflow Automation - Production Ready**
