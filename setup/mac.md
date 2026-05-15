# Mac Setup Guide

## 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. Install Miniconda

```bash
brew install miniconda
```

Then initialize conda for your shell:

```bash
conda init zsh      # or: conda init bash
```

Restart your terminal, then verify: `conda --version`

## 3. Install Git

Git comes pre-installed on Mac. Verify with `git --version`.  
If missing: `brew install git`

## 4. Install Ollama

```bash
brew install ollama
```

Or download directly from: https://ollama.com/download/mac

## 5. Create the Conda Environment

Open a terminal in the project folder:

```bash
conda env create -f environment.yml
conda activate localai
```

## 6. Apple Silicon (M1/M2/M3) — GPU Acceleration

PyTorch automatically uses **MPS (Metal Performance Shaders)** on Apple Silicon — no extra steps needed. Your models will run significantly faster than CPU-only.

To verify MPS is available in a notebook:

```python
import torch
print(torch.backends.mps.is_available())  # Should print: True
```

> Note: Use `device = "mps"` instead of `"cuda"` in PyTorch code on Mac.

## 7. Launch JupyterLab

```bash
conda activate localai
jupyter lab
```

## 8. Pull Your First LLM

In a separate terminal:

```bash
ollama serve         # start the server (if not auto-started)
ollama pull llama3.2:3b    # ~2GB, fast and capable
```

Then run `notebooks/04_local_llms/01_ollama_chat.ipynb` to test it.

---

## Syncing with GitHub

```bash
# Clone the repo (first time)
git clone https://github.com/YOUR_USERNAME/LocalAI.git
cd LocalAI

# After making changes
git add .
git commit -m "your message"
git push
```
