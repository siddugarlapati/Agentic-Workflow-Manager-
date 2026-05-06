# Training Notebooks

This directory contains Jupyter notebooks for setting up and training local models for the Workflow Manager.

**100% Local - No API Keys Required**

## Notebooks

### 1. Model Setup (`01_model_setup.ipynb`)
- Install and configure Ollama
- Pull local models (Llama 3.1, Mistral, etc.)
- Test model performance
- Configure for Workflow Manager

**Use this first** to set up your local LLM environment.

### 2. Model Fine-tuning (`02_model_finetuning.ipynb`)
- Fine-tune models on workflow tasks
- Use LoRA for efficient training
- Test fine-tuned models
- Export for Ollama

**Use this** to improve model performance on your specific workflows.

### 3. Workflow Data Collection (`03_workflow_data_collection.ipynb`)
- Extract training data from executions
- Create planning examples
- Create validation examples
- Generate synthetic data

**Use this** to collect training data from your actual workflow executions.

## Quick Start

### Option 1: Local Jupyter

```bash
# Install Jupyter
pip install jupyter

# Start Jupyter
cd notebooks
jupyter notebook

# Open 01_model_setup.ipynb
```

### Option 2: VS Code

1. Install Python extension
2. Open notebook file
3. Select Python kernel
4. Run cells

### Option 3: JupyterLab

```bash
pip install jupyterlab
jupyter lab
```

## Requirements

```bash
pip install jupyter notebook jupyterlab
pip install torch transformers datasets peft accelerate
pip install ollama langchain langchain-community
pip install psycopg2-binary pandas
```

## Workflow

```
1. Setup Local Models
   ↓
   Run: 01_model_setup.ipynb
   ↓
2. Collect Training Data
   ↓
   Run: 03_workflow_data_collection.ipynb
   ↓
3. Fine-tune Model
   ↓
   Run: 02_model_finetuning.ipynb
   ↓
4. Deploy Fine-tuned Model
   ↓
   Update OLLAMA_MODEL in .env
```

## Model Recommendations

### Development (8GB RAM)
- **llama3.1** (8B) - Best balance
- **mistral** (7B) - Faster
- **phi3** (3.8B) - Lightweight

### Production (16GB+ RAM)
- **llama3.1:70b** - Best quality
- **mixtral** - Good balance

### Fine-tuning
- **phi-2** (2.7B) - Fast to train
- **TinyLlama** (1.1B) - Very fast

## Privacy & Security

✅ All models run locally
✅ No data sent to external APIs
✅ No API keys required
✅ Complete control over data
✅ GDPR/HIPAA compliant

## Tips

### Memory Management
- Close other applications
- Use smaller models for testing
- Enable GPU if available
- Use LoRA for efficient fine-tuning

### Training Data
- Start with 50-100 examples
- Add more as you collect executions
- Balance different task types
- Include both success and failure cases

### Model Selection
- Start with smaller models
- Test on your specific tasks
- Fine-tune if needed
- Scale up for production

## Troubleshooting

### Ollama Not Running
```bash
# Start Ollama service
ollama serve

# Check status
ollama list
```

### Out of Memory
- Use smaller model
- Reduce batch size
- Enable gradient checkpointing
- Use CPU instead of GPU

### Slow Training
- Use GPU if available
- Reduce model size
- Use LoRA instead of full fine-tuning
- Reduce training data size

## Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [PEFT (LoRA) Documentation](https://huggingface.co/docs/peft)

## Support

For issues or questions:
1. Check notebook comments
2. Review error messages
3. Consult documentation
4. Open GitHub issue

---

**Start with notebook 01 to set up your local models!**
