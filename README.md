# LocalAI — AI Tinkering Project

A beginner-friendly workspace for learning and experimenting with:
- **Local LLMs** (Ollama — run AI models on your own machine)
- **Classical Machine Learning** (scikit-learn, data analysis)
- **Deep Learning** (PyTorch)
- **Computer Vision** (images, torchvision, OpenCV)

Works on Windows and Mac. Synced via Git + GitHub.

---

## Quick Start

### 1. Install Prerequisites

| Tool | Windows | Mac |
|------|---------|-----|
| Miniconda | [miniconda.pypa.io](https://docs.conda.io/en/latest/miniconda.html) | `brew install miniconda` |
| Git | [git-scm.com](https://git-scm.com) | `brew install git` |
| Ollama | [ollama.com](https://ollama.com) | `brew install ollama` |

See `setup/windows.md` or `setup/mac.md` for detailed steps.

### 2. Create the Conda Environment

```bash
conda env create -f environment.yml
conda activate localai
```

This installs Python 3.11 + all ML libraries. Only needs to be done once per machine.

### 3. Launch JupyterLab

```bash
conda activate localai
jupyter lab
```

Open `http://localhost:8888` in your browser. Start with the `notebooks/` folder.

### 4. Pull a Local LLM (Ollama)

```bash
# In a separate terminal
ollama serve          # start the Ollama server

# Pull a small model (~2GB) to start
ollama pull llama3.2:3b
```

Then run `notebooks/04_local_llms/01_ollama_chat.ipynb` or `scripts/ollama_chat.py`.

---

## Project Structure

```
LocalAI/
├── notebooks/
│   ├── 01_classical_ml/    ← Start here: pandas + scikit-learn
│   ├── 02_deep_learning/   ← Neural networks with PyTorch
│   ├── 03_computer_vision/ ← Images and visual AI
│   └── 04_local_llms/      ← Run LLMs locally with Ollama
├── scripts/
│   └── ollama_chat.py      ← Terminal chat with your local model
├── data/                   ← Put small datasets here
├── models/                 ← (gitignored) large model files
├── setup/
│   ├── windows.md
│   └── mac.md
└── environment.yml         ← Conda environment
```

## Syncing Between Machines

```bash
# After working on one machine, save your changes:
git add .
git commit -m "describe what you worked on"
git push

# On the other machine, get the latest:
git pull
```

Notebook outputs are saved in `.ipynb` files — they'll sync automatically.

---

## Learning Path (Suggested Order)

1. `notebooks/01_classical_ml/01_pandas_intro.ipynb` — load and explore data
2. `notebooks/01_classical_ml/02_sklearn_basics.ipynb` — train your first ML model
3. `notebooks/04_local_llms/01_ollama_chat.ipynb` — talk to a local AI
4. `notebooks/02_deep_learning/01_pytorch_intro.ipynb` — understand neural networks
5. `notebooks/03_computer_vision/01_image_basics.ipynb` — work with images
6. `notebooks/04_local_llms/02_simple_rag.ipynb` — build a simple RAG pipeline
