import requests
import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Query a local Ollama model with streaming response.")
parser.add_argument("prompt", type=str, help="The prompt to send to the model.")
parser.add_argument("--model", type=str, default="llama3", help="Model name (default: llama3)")
args = parser.parse_args()

# Send a streaming request to the local Ollama server
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": args.model,
        "prompt": args.prompt,
        "stream": True
    },
    stream=True
)

# Parse and print the streaming response
if response.status_code == 200:
    print(f"Response from {args.model} (streaming):\n")
    for line in response.iter_lines(decode_unicode=True):
        if line.strip():
            try:
                data = json.loads(line)
                print(data.get("response", ""), end="", flush=True)
            except Exception as e:
                print("\n[Error parsing stream chunk]:", e)
else:
    print("Error:", response.status_code, response.text)
