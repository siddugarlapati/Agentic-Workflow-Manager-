# Local Model Training Guide

Complete guide for training and fine-tuning local models for the Workflow Manager.

**🔒 100% Local - No API Keys Required - Complete Privacy**

## Overview

This project uses **local LLM models** via Ollama, ensuring:
- ✅ No data sent to external APIs
- ✅ No API keys or subscriptions needed
- ✅ Complete control over your data
- ✅ GDPR/HIPAA compliant
- ✅ Unlimited usage at no cost

## Quick Start

### 1. Install Ollama

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama
ollama serve
```

### 2. Pull a Model

```bash
# Recommended for development (8GB RAM)
ollama pull llama3.1

# For better quality (16GB+ RAM)
ollama pull llama3.1:70b

# For faster responses (4GB RAM)
ollama pull mistral
```

### 3. Configure Workflow Manager

```bash
# Edit backend/.env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1
```

That's it! No API keys needed.

## Training Notebooks

We provide 3 Jupyter notebooks for model training:

### 📓 Notebook 1: Model Setup
**File**: `notebooks/01_model_setup.ipynb`

**What it does**:
- Installs Ollama
- Downloads local models
- Tests model performance
- Compares different models
- Configures for Workflow Manager

**When to use**: First time setup

### 📓 Notebook 2: Model Fine-tuning
**File**: `notebooks/02_model_finetuning.ipynb`

**What it does**:
- Fine-tunes models on workflow tasks
- Uses LoRA for efficient training
- Creates workflow-specific models
- Exports for Ollama
- Tests fine-tuned performance

**When to use**: To improve model performance on your workflows

### 📓 Notebook 3: Data Collection
**File**: `notebooks/03_workflow_data_collection.ipynb`

**What it does**:
- Extracts training data from executions
- Creates planning examples
- Creates validation examples
- Generates synthetic data
- Exports in multiple formats

**When to use**: To collect training data from your actual workflow executions

## Training Workflow

```
┌─────────────────────────────────────────┐
│ 1. Setup Local Models                   │
│    Run: 01_model_setup.ipynb           │
│    - Install Ollama                     │
│    - Pull models                        │
│    - Test performance                   │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────▼──────────────────────────┐
│ 2. Use Default Model                    │
│    - Start with llama3.1                │
│    - Run workflows                      │
│    - Collect execution data             │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────▼──────────────────────────┐
│ 3. Collect Training Data                │
│    Run: 03_workflow_data_collection.ipynb│
│    - Extract from database              │
│    - Create examples                    │
│    - Generate synthetic data            │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────▼──────────────────────────┐
│ 4. Fine-tune Model                      │
│    Run: 02_model_finetuning.ipynb      │
│    - Load base model                    │
│    - Train with LoRA                    │
│    - Test performance                   │
│    - Export for Ollama                  │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────▼──────────────────────────┐
│ 5. Deploy Fine-tuned Model              │
│    - Update OLLAMA_MODEL in .env        │
│    - Restart backend                    │
│    - Monitor performance                │
└─────────────────────────────────────────┘
```

## Model Recommendations

### For Development (8GB RAM)
```bash
# Best balance of quality and speed
ollama pull llama3.1

# Faster, smaller
ollama pull mistral

# Very lightweight
ollama pull phi3
```

### For Production (16GB+ RAM)
```bash
# Best quality
ollama pull llama3.1:70b

# Good balance
ollama pull mixtral
```

### For Code Tasks
```bash
# Optimized for code
ollama pull codellama

# Alternative
ollama pull deepseek-coder
```

### For Fine-tuning
```bash
# Fast to train (2.7B params)
# Use in notebook 02
microsoft/phi-2

# Very fast (1.1B params)
TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

## Fine-tuning Benefits

### Why Fine-tune?

1. **Better Performance**: Models learn your specific workflow patterns
2. **Faster Execution**: Optimized for your use cases
3. **More Accurate**: Understands your domain terminology
4. **Cost Effective**: One-time training, unlimited usage
5. **Privacy**: Training data never leaves your infrastructure

### What Improves?

- **Planning**: Better workflow step generation
- **Validation**: More accurate error detection
- **Correction**: Smarter parameter fixes
- **Tool Selection**: Better tool choice for tasks

### Example Results

**Before Fine-tuning**:
```
Task: Create Jira project for client
Output: "I'll help you create a project..."
(Generic response, needs clarification)
```

**After Fine-tuning**:
```
Task: Create Jira project for client
Output: {
  "tool": "jira_create_project",
  "parameters": {
    "project_key": "CLIENT",
    "project_name": "Client Project",
    "lead_account_id": "user123"
  }
}
(Specific, actionable response)
```

## Training Data

### What Data to Collect?

1. **Successful Executions**: Learn correct patterns
2. **Failed Executions**: Learn error handling
3. **Corrections**: Learn self-correction patterns
4. **Validations**: Learn quality checks

### How Much Data?

- **Minimum**: 50-100 examples
- **Good**: 500-1000 examples
- **Excellent**: 5000+ examples

Start small and iterate!

### Data Privacy

All training data:
- ✅ Stays in your database
- ✅ Never sent to external services
- ✅ Fully under your control
- ✅ Can be anonymized if needed

## Hardware Requirements

### Minimum (Development)
- **CPU**: 4 cores
- **RAM**: 8GB
- **Storage**: 10GB
- **GPU**: Optional

### Recommended (Production)
- **CPU**: 8+ cores
- **RAM**: 16GB+
- **Storage**: 50GB SSD
- **GPU**: NVIDIA with 8GB+ VRAM (optional but faster)

### For Fine-tuning
- **CPU**: 8+ cores
- **RAM**: 16GB+ (32GB recommended)
- **Storage**: 50GB SSD
- **GPU**: NVIDIA with 16GB+ VRAM (highly recommended)

## Cost Analysis

### Traditional API-based Solution
```
OpenAI GPT-4:
- $0.03 per 1K input tokens
- $0.06 per 1K output tokens
- 1000 workflows/day = ~$50-100/day
- Monthly cost: $1,500-3,000
- Annual cost: $18,000-36,000
```

### Local Model Solution
```
One-time costs:
- Hardware: $0 (use existing) to $2,000 (GPU server)
- Setup time: 1-2 hours
- Training time: 2-4 hours (optional)

Ongoing costs:
- Electricity: ~$10-20/month
- Maintenance: Minimal

Annual cost: $120-240 (electricity only)
Savings: $17,880-35,880 per year
```

## Performance Comparison

### Response Time
- **API-based**: 2-5 seconds (network latency)
- **Local model**: 0.5-2 seconds (no network)

### Throughput
- **API-based**: Rate limited (e.g., 60 req/min)
- **Local model**: Hardware limited (100+ req/min)

### Availability
- **API-based**: Depends on service uptime
- **Local model**: 100% under your control

## Security & Compliance

### Data Privacy
- ✅ No data leaves your infrastructure
- ✅ No third-party access
- ✅ Complete audit trail
- ✅ GDPR compliant
- ✅ HIPAA compliant
- ✅ SOC 2 ready

### Model Security
- ✅ Models stored locally
- ✅ No external dependencies
- ✅ Version controlled
- ✅ Reproducible builds

## Troubleshooting

### Ollama Not Starting
```bash
# Check if running
ps aux | grep ollama

# Start manually
ollama serve

# Check logs
journalctl -u ollama -f
```

### Model Not Loading
```bash
# List available models
ollama list

# Pull model again
ollama pull llama3.1

# Check disk space
df -h
```

### Out of Memory
```bash
# Use smaller model
ollama pull mistral

# Or reduce context window
# Edit Modelfile:
PARAMETER num_ctx 2048
```

### Slow Performance
```bash
# Check CPU usage
top

# Use GPU if available
# Ollama automatically uses GPU

# Reduce model size
ollama pull phi3
```

## Best Practices

### 1. Start Simple
- Begin with default llama3.1
- Run workflows and collect data
- Fine-tune only when needed

### 2. Collect Quality Data
- Focus on successful executions
- Include error cases
- Add synthetic examples
- Balance different task types

### 3. Iterate
- Train on small dataset first
- Test performance
- Collect more data
- Retrain and improve

### 4. Monitor Performance
- Track execution success rate
- Measure response time
- Log agent decisions
- Analyze errors

### 5. Version Control
- Save training data
- Version fine-tuned models
- Document changes
- Enable rollback

## Resources

### Documentation
- [Ollama Docs](https://ollama.ai/docs)
- [LangChain Docs](https://python.langchain.com/)
- [Transformers Docs](https://huggingface.co/docs/transformers)
- [LoRA/PEFT Docs](https://huggingface.co/docs/peft)

### Models
- [Ollama Model Library](https://ollama.ai/library)
- [Hugging Face Models](https://huggingface.co/models)

### Community
- [Ollama GitHub](https://github.com/ollama/ollama)
- [LangChain Community](https://github.com/langchain-ai/langchain)

## Next Steps

1. **Setup**: Run `notebooks/01_model_setup.ipynb`
2. **Use**: Start running workflows with default model
3. **Collect**: Run `notebooks/03_workflow_data_collection.ipynb`
4. **Train**: Run `notebooks/02_model_finetuning.ipynb`
5. **Deploy**: Update `.env` and restart

## Support

For questions or issues:
1. Check notebook comments
2. Review this guide
3. Consult Ollama docs
4. Open GitHub issue

---

**Start training your local models today - no API keys required!**
