# Project 10: Mini GPT (Transformer Language Model)

Welcome to **Project 10**! In this project, you will build a GPT-style transformer language model from scratch.

This project builds directly on the concepts from **Project 09 (LSTM Text Generation)**. We will use the exact same Shakespeare dataset so that you can directly compare how a Transformer learns differently (and better!) than an LSTM.

## What You Will Build

You will implement the core components of the Transformer architecture that power modern LLMs (GPT-4, Claude, Gemini, etc.):

- **Self-Attention** — query, key, value projections with scaled dot-product
- **Multi-Head Attention** — multiple attention patterns running in parallel
- **Positional Encoding** — sinusoidal encoding to inject position information
- **Transformer Blocks** — layer normalization, feed-forward networks, and residual connections
- **Attention Visualization** — real heatmaps showing what the model "sees"

By the end of this notebook, you will have trained a GPT-style language model capable of generating Shakespearean text — and you'll understand the exact architecture behind every modern LLM.

---

## Setup Instructions (Windows & macOS)

### Prerequisites

- **Python 3.11** (via conda, recommended)
- **Git** (to clone the repo)

### Option 1: Using conda (Recommended)

```bash
# 1. Navigate to the project root
cd LocalAI

# 2. Create the environment (first time only)
conda env create -f environment.yml

# 3. Activate the environment
conda activate localai

# 4. Launch Jupyter Lab
jupyter lab
```

### Option 2: Using pip (if you already have Python 3.11+)

```bash
# 1. Navigate to the project root
cd LocalAI

# 2. Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install numpy matplotlib jupyterlab tqdm

# 3. Launch Jupyter Lab
jupyter lab
```

> **Note:** `environment.yml` installs the CPU-only PyTorch build by default, which works on both Windows and macOS. If you have an NVIDIA GPU, see the [GPU Setup](#gpu-setup-optional) section below.

### Running the Notebook

1. In Jupyter Lab, navigate to `notebooks/05_projects/10_mini_gpt/mini_gpt.ipynb`
2. Run the cells **in order** from top to bottom
3. **First-run tip:** The notebook defaults to `TRAINING_MODE = "quick"` — a 3-epoch demo that completes in ~3-5 minutes on CPU. Once you're ready for the full experience, change it to `"full"` and re-run.

---

## Quick Start Summary

| Step | Action | Time |
|------|--------|------|
| 1 | Create & activate conda environment | ~2 min |
| 2 | Open notebook & run Setup cells | ~30 sec |
| 3 | Run Parts 1-5 (architecture) | ~1 min |
| 4 | Run Part 6 (training — quick mode) | ~3-5 min CPU / ~1-2 min GPU |
| 5 | Run Parts 7-8 (generation & attention viz) | ~2 min |
| **Total (quick mode)** | **~10 minutes** | |

---

## Cross-Platform Notes

| Feature | Windows | macOS |
|---------|---------|-------|
| GPU acceleration | CUDA (NVIDIA GPU) | MPS (Apple Silicon) |
| Fallback | CPU (always works) | CPU (always works) |
| `KMP_DUPLICATE_LIB_OK` | Not needed, not set | Automatically set to prevent crashes |
| Path handling | Project-relative paths — works anywhere | Project-relative paths — works anywhere |
| Data download | Project Gutenberg (auto) | Project Gutenberg (auto) |

---

## GPU Setup (Optional)

### Windows with NVIDIA GPU

```bash
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### macOS with Apple Silicon (M1/M2/M3/M4)

MPS support is included in the default PyTorch install. The notebook automatically detects and uses MPS if available. No extra steps needed.

---

## Key Sections in the Notebook

| Part | Topic | What You'll Do |
|------|-------|---------------|
| Setup | Environment check | Verify all packages are installed |
| 1 | Load Shakespeare | Download & preprocess the same dataset as Project 09 |
| 2 | Tokenization | Character-level encoding |
| 3 | Dataset prep | Create DataLoader with sliding windows |
| 4 | Self-Attention | **The key concept** — understand Q, K, V |
| 5 | Build the transformer | Implement each component from scratch |
| 6 | Training | Train with warmup + cosine decay, tqdm progress bars |
| 7 | Text generation | Generate Shakespearean text at different temperatures |
| 8 | Attention visualization | **NEW** — real heatmaps of attention patterns |
| 9 | Comparison | LSTM vs Transformer side-by-side |

---

## Improvements Over the Original Notebook

| Improvement | Benefit |
|-------------|---------|
| Project-relative paths | Works on any machine regardless of folder name |
| Environment check cell | Friendly error messages if packages are missing |
| `TRAINING_MODE` toggle | Quick demo (3 epochs) or full training (15 epochs) |
| `tqdm` progress bars | See real-time training progress |
| Best-model checkpointing | Saves model with lowest perplexity, not just the last epoch |
| Real attention visualization | Working heatmaps showing head-specific and averaged attention patterns |
| macOS-specific `KMP_DUPLICATE_LIB_OK` | Only set when actually needed |
| MPS try/except fallback | Handles edge cases on older Macs gracefully |
| Download failure handling | Clear troubleshooting instructions |

---

## Troubleshooting

### "No module named 'torch'"
Your conda environment isn't activated. Run: `conda activate localai`

### "No module named 'tqdm'"
Install it: `pip install tqdm`

### Training is too slow on CPU
Switch `TRAINING_MODE = "quick"` (the default). This uses a smaller model (3 layers, 128-dim embeddings) for 3 epochs.

### MPS errors on macOS
The notebook catches MPS initialization failures and falls back to CPU automatically. If you still see issues, ensure your PyTorch is up to date: `pip install --upgrade torch`

### Out of memory (CUDA)
Reduce batch size: in the Setup cell, you can manually set `QUICK_BATCH = 16` or lower.

### Data download fails
The notebook will print clear instructions with the exact path to place a manually downloaded `pg100.txt` file.

---

## Comparison with Project 09

| | LSTM (Project 09) | Transformer (Project 10) |
|---|---|---|
| Parameters | ~1M | ~0.5M (quick) / ~5M (full) |
| Training speed | Slower (sequential) | Faster (parallel over sequence) |
| Generation speed | Fast per token (O(1)) | Slower per token (O(n²)) |
| Long-range context | Struggles beyond ~50 chars | Strong at any distance in context |
| Interpretability | Hidden state is opaque | Attention weights are visualizable |

---

## Resources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — the original transformer paper
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar's visual guide
- [nanoGPT](https://github.com/karpathy/nanoGPT) — Andrej Karpathy's minimal GPT implementation
- [Let's Build GPT from Scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Karpathy's video walkthrough