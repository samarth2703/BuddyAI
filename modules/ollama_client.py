import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

class OllamaClient:
    def __init__(self, model="llama3.2:1b"):
        self.model = model

    def ask(self, prompt):
        print("\n[DEBUG] Sending to Ollama:", prompt)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                OLLAMA_URL,
                json=payload,
                timeout=200
            )

            print("[DEBUG] Status:", response.status_code)
            print("[DEBUG] Raw Response:", response.text)

            # If server returned an error message
            if response.status_code != 200:
                return "AI Error: " + response.text

            data = response.json()

            # Try all response formats
            reply = (
                data.get("response") or
                data.get("output") or
                data.get("content") or
                data.get("message", {}).get("content")
            )

            if not reply:
                return "AI returned empty response."

            return reply.strip()

        except Exception as e:
            print("[OLLAMA ERROR]", e)
            return "Could not connect to AI engine."
