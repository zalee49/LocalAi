# Graph Report - .  (2026-06-08)

## Corpus Check
- Corpus is ~32,847 words - fits in a single context window. You may not need a graph.

## Summary
- 32 nodes · 42 edges · 7 communities (5 shown, 2 thin omitted)
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.84)
- Token cost: 76,105 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Mini-GPT Model & Project|Mini-GPT Model & Project]]
- [[_COMMUNITY_Transformer Architecture|Transformer Architecture]]
- [[_COMMUNITY_Ollama Terminal Chat|Ollama Terminal Chat]]
- [[_COMMUNITY_Project Setup & Environment|Project Setup & Environment]]
- [[_COMMUNITY_Character Dataset (Shakespeare)|Character Dataset (Shakespeare)]]
- [[_COMMUNITY_LR Schedule|LR Schedule]]

## God Nodes (most connected - your core abstractions)
1. `MiniGPT` - 7 edges
2. `main()` - 5 edges
3. `Ollama HTTP API (localhost:11434)` - 4 edges
4. `MultiHeadAttention` - 4 edges
5. `TransformerBlock` - 4 edges
6. `Mini GPT Project README` - 4 edges
7. `localai conda environment spec` - 4 edges
8. `LocalAI Project README` - 4 edges
9. `Mac Setup Guide` - 4 edges
10. `Windows Setup Guide` - 4 edges

## Surprising Connections (you probably didn't know these)
- `MiniGPT` --semantically_similar_to--> `nanoGPT (Karpathy)`  [INFERRED] [semantically similar]
  formatted_mini_gpt.json → notebooks/05_projects/10_mini_gpt/README.md
- `LocalAI Project README` --references--> `main()`  [INFERRED]
  README.md → scripts/ollama_chat.py
- `localai Conda Environment Convention` --conceptually_related_to--> `Ollama HTTP API (localhost:11434)`  [INFERRED]
  CLAUDE.md → scripts/ollama_chat.py
- `MiniGPT` --implements--> `Cross-Platform Device Detection (cuda/mps/cpu)`  [INFERRED]
  formatted_mini_gpt.json → CLAUDE.md
- `Mini GPT Project README` --references--> `MiniGPT`  [INFERRED]
  notebooks/05_projects/10_mini_gpt/README.md → formatted_mini_gpt.json

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **MiniGPT Transformer Architecture** — formatted_mini_gpt_minigpt, formatted_mini_gpt_transformerblock, formatted_mini_gpt_multiheadattention, formatted_mini_gpt_feedforward, formatted_mini_gpt_positionalencoding [EXTRACTED 1.00]
- **Ollama Terminal Chat REPL Flow** — scripts_ollama_chat_main, scripts_ollama_chat_check_ollama, scripts_ollama_chat_stream_chat, scripts_ollama_chat_ollama_http_api [EXTRACTED 1.00]
- **Cross-Platform Setup (conda + device detection)** — environment_localai, setup_mac, setup_windows, claude_device_detection [INFERRED 0.85]

## Communities (7 total, 2 thin omitted)

### Community 0 - "Mini-GPT Model & Project"
Cohesion: 0.32
Nodes (8): Mini GPT Project README, nanoGPT (Karpathy), TRAINING_MODE toggle (quick/full), Attention Is All You Need, generate_text, MiniGPT, PositionalEncoding, Weight Tying (embedding / LM head)

### Community 1 - "Transformer Architecture"
Cohesion: 0.38
Nodes (7): Causal Masking, FeedForward, MultiHeadAttention, Residual Connections + LayerNorm, Self-Attention (scaled dot-product), SelfAttention, TransformerBlock

### Community 2 - "Ollama Terminal Chat"
Cohesion: 0.52
Nodes (6): check_ollama(), list_models(), main(), Ollama HTTP API (localhost:11434), Terminal chat interface for a local Ollama model.  Usage:     python ollama_chat, stream_chat()

### Community 3 - "Project Setup & Environment"
Cohesion: 0.60
Nodes (6): Cross-Platform Device Detection (cuda/mps/cpu), localai Conda Environment Convention, localai conda environment spec, LocalAI Project README, Mac Setup Guide, Windows Setup Guide

## Knowledge Gaps
- **5 isolated node(s):** `FeedForward`, `CharDataset`, `generate_text`, `get_lr (warmup + cosine decay LR schedule)`, `Shakespeare Dataset (Project Gutenberg pg100)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MiniGPT` connect `Mini-GPT Model & Project` to `Transformer Architecture`, `Project Setup & Environment`?**
  _High betweenness centrality (0.525) - this node is a cross-community bridge._
- **Why does `Cross-Platform Device Detection (cuda/mps/cpu)` connect `Project Setup & Environment` to `Mini-GPT Model & Project`?**
  _High betweenness centrality (0.387) - this node is a cross-community bridge._
- **Why does `TransformerBlock` connect `Transformer Architecture` to `Mini-GPT Model & Project`?**
  _High betweenness centrality (0.290) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `MiniGPT` (e.g. with `Mini GPT Project README` and `nanoGPT (Karpathy)`) actually correct?**
  _`MiniGPT` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Terminal chat interface for a local Ollama model.  Usage:     python ollama_chat`, `FeedForward`, `CharDataset` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._