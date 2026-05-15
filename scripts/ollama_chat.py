"""
Terminal chat interface for a local Ollama model.

Usage:
    python ollama_chat.py
    python ollama_chat.py --model phi3:mini
    python ollama_chat.py --system "You are a pirate"

Requires Ollama running: ollama serve
Pull a model first: ollama pull llama3.2:3b
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2:3b"


def check_ollama():
    try:
        requests.get(f"{OLLAMA_URL}/", timeout=3)
    except requests.exceptions.ConnectionError:
        print("Error: Ollama is not running.")
        print("Start it with: ollama serve")
        sys.exit(1)


def list_models():
    response = requests.get(f"{OLLAMA_URL}/api/tags")
    models = response.json().get("models", [])
    if not models:
        print("No models downloaded. Run: ollama pull llama3.2:3b")
    else:
        print("Available models:")
        for m in models:
            size_gb = m.get("size", 0) / 1e9
            print(f"  {m['name']}  ({size_gb:.1f} GB)")


def stream_chat(messages, model):
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": model, "messages": messages, "stream": True},
        stream=True,
    )

    full_reply = ""
    print("Assistant: ", end="", flush=True)

    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            token = chunk.get("message", {}).get("content", "")
            print(token, end="", flush=True)
            full_reply += token
            if chunk.get("done", False):
                break

    print()  # newline after response
    return full_reply


def main():
    parser = argparse.ArgumentParser(description="Chat with a local Ollama model")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model to use")
    parser.add_argument("--system", default=None, help="System prompt")
    parser.add_argument("--list", action="store_true", help="List available models")
    args = parser.parse_args()

    check_ollama()

    if args.list:
        list_models()
        return

    print(f"Model: {args.model}")
    print("Type your message and press Enter. Type 'quit' or Ctrl+C to exit.")
    print("-" * 50)

    history = []
    if args.system:
        history.append({"role": "system", "content": args.system})
        print(f"System: {args.system}\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        if user_input.lower() == "/clear":
            history = [m for m in history if m["role"] == "system"]
            print("(conversation cleared)")
            continue

        if user_input.lower() == "/history":
            for msg in history:
                if msg["role"] != "system":
                    print(f"{msg['role'].capitalize()}: {msg['content']}")
            continue

        history.append({"role": "user", "content": user_input})
        reply = stream_chat(history, args.model)
        history.append({"role": "assistant", "content": reply})
        print()


if __name__ == "__main__":
    main()
