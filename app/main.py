import sys
import threading
import tkinter as tk
from tkinter import scrolledtext

# Allow imports from /modules
sys.path.append("./modules")

from speech_to_text import SpeechToText
from text_to_speech import speak
from ollama_client import OllamaClient
from search_online import web_search
from windows_controller import handle_windows_action


# Create Ollama client once
ollama = OllamaClient(model="llama3.2:1b")


# ---------------------------
#  PROCESS USER COMMAND
# ---------------------------
def process_command(text, ui_box):
    text = text.lower().strip()

    ui_box.insert(tk.END, f"\nYou: {text}\n")
    ui_box.see(tk.END)

    # 1. Windows actions (open app / website / shutdown / etc)
    action = handle_windows_action(text)
    if action:
        ui_box.insert(tk.END, f"Buddy: {action}\n")
        ui_box.see(tk.END)
        speak(action)
        return

    # 2. Online search
    if "search" in text or "google" in text:
        query = text.replace("search", "").replace("google", "").strip()
        result = web_search(query)

        ui_box.insert(tk.END, f"Buddy (Search): {result}\n")
        ui_box.see(tk.END)
        speak(result)
        return

    # 3. Offline AI using Ollama
    reply = ollama.ask(text)

    ui_box.insert(tk.END, f"Buddy: {reply}\n")
    ui_box.see(tk.END)
    speak(reply)


# ---------------------------
#  UI + VOICE LOOP
# ---------------------------
def start_app():
    root = tk.Tk()
    root.title("Buddy AI")
    root.geometry("500x600")

    chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 12))
    chat_box.pack(fill=tk.BOTH, expand=True)

    chat_box.insert(tk.END, "Buddy: Hello, I am Buddy. Say something...\n")

    # Start Speech-to-Text
    stt = SpeechToText(model_path="models/vosk-model-small-en-in-0.4")

    def callback(text):
        process_command(text, chat_box)

    threading.Thread(target=lambda: stt.start_listening(callback), daemon=True).start()

    root.mainloop()


if __name__ == "__main__":
    start_app()
