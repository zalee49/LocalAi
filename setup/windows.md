# Windows Setup Guide

## 1. Install Miniconda

1. Download the Windows installer from: https://docs.conda.io/en/latest/miniconda.html  
   → Choose **Miniconda3 Windows 64-bit**
2. Run the `.exe` installer
3. During install: check **"Add Miniconda3 to my PATH"** (or use Anaconda Prompt)
4. Verify: open a new terminal and run `conda --version`

## 2. Install Git

1. Download from: https://git-scm.com/download/win
2. Run installer, default settings are fine
3. Verify: `git --version`

## 3. Install Ollama

1. Download from: https://ollama.com/download/windows
2. Run the installer — Ollama runs as a background service automatically
3. Verify: open a terminal and run `ollama --version`

## 4. Create the Conda Environment

Open a terminal (Anaconda Prompt, PowerShell, or Git Bash) in the project folder:

```bash
conda env create -f environment.yml
conda activate localai
```

> This takes a few minutes the first time. Only needed once per machine.

## 5. (Optional) Enable GPU Acceleration

If you have an **Nvidia GPU**, reinstall PyTorch with CUDA support after creating the environment:

```bash
conda activate localai
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Check your CUDA version first: `nvidia-smi`

## 6. Launch JupyterLab

```bash
conda activate localai
jupyter lab
```

## 7. Pull Your First LLM

In a separate terminal:

```bash
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
