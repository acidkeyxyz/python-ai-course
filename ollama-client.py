import requests

def main():
    # Configuration
    MODEL = 'qwen3:8b'  # You can change this to any model available on your Ollama server
    BASE_URL = 'http://localhost:11434/api/generate'

    # Prompt input from the user
    prompt = input("Enter your prompt: ")

    # Prepare request payload
    payload = {
        'model': MODEL,
        'prompt': prompt
    }

    # Send POST request to Ollama server
    try:
        response = requests.post(BASE_URL, json=payload, stream=True, timeout=60)
        response.raise_for_status()

        print("\nGenerated Text:")
        import json
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                print(chunk.get('response', ''), end='', flush=True)
        print()

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama server: {e}")

if __name__ == "__main__":
    main()

