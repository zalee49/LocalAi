# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

Conda environment name: `localai` (Python 3.11). All work runs inside JupyterLab.

```bash
conda activate localai
jupyter lab                # opens http://localhost:8888
```

To add a package:
```bash
conda activate localai
pip install <package>
```

For GPU-accelerated PyTorch on Windows (Nvidia):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Cross-Platform Rules

This repo runs on both Windows (CUDA) and Mac (MPS). All code must work on both without modification.

**Device detection** — every PyTorch notebook uses this pattern:
```python
if torch.cuda.is_available():
    device = torch.device('cuda')
elif torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')
```

**File paths** — always use `pathlib.Path` with `Path.home()` as the root anchor:
```python
data_dir = Path.home() / "LocalAI" / "data"
```

**DataLoader workers** — `num_workers=4` works in Jupyter on both platforms. The `if __name__ == '__main__':` guard is only needed in `.py` scripts on Windows.

## Project Structure

```
notebooks/
  01_classical_ml/     ← pandas, scikit-learn
  02_deep_learning/    ← PyTorch basics
  03_computer_vision/  ← images, torchvision
  04_local_llms/       ← Ollama chat + RAG
  05_projects/         ← hands-on projects (MNIST, CIFAR-100, tabular ML)
scripts/
  ollama_chat.py       ← terminal chat with local LLM
data/                  ← small datasets (gitignored large files)
models/                ← saved checkpoints (gitignored)
environment.yml        ← conda spec
```

## Deep Learning Conventions

Projects in `notebooks/05_projects/` follow a consistent pattern:
- Data downloaded via torchvision/sklearn into `Path.home() / "LocalAI" / "data"`
- Checkpoints saved to `Path.home() / "LocalAI" / "models" / <project>`
- `pin_memory=True` on DataLoaders when using GPU
- SGD + CosineAnnealingLR + label smoothing is the preferred training setup for CNN projects

## Local LLMs (Ollama)

Ollama must be running before executing LLM notebooks:
```bash
ollama serve           # Mac: may need this; Windows: runs as background service
ollama pull llama3.2:3b
```
