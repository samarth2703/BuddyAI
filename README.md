
---

# 🌟 **Buddy AI — Your Personal Desktop AI Agent (Offline + Voice Controlled)**

A fully offline-capable, voice-controlled AI assistant that can think, speak, search the internet, and control your Windows system — all running locally on your PC.

Buddy AI is lightweight, fast, privacy-friendly, and customizable.
 <br>                                                                                                      _ made by - Samarth!!!
---

<div align="center">

### 🧠 **Offline AI Engine**

### 🎤 Voice Recognition

### 🗣️ Text-to-Speech

### 🌐 Online Search

### 🪟 Windows App Controller

### 🤖 Built on Local LLM (Ollama)

</div>

---

# 🚀 **Features**

## 🧠 **1. Offline AI Chat (Local LLM)**

Buddy uses **Ollama** with the model:

```
llama3.2:1b
```

This model gives:

* Low RAM usage
* Fast responses
* No internet required
* Zero data sharing
* Works even without GPU

Perfect for offline personal assistants.

---

## 🎤 **2. Voice Input (Speech-to-Text)**

**Tools Used:**
✔ `Vosk` (models/vosk-model-small-en-in-0.4)
✔ `sounddevice`

Features:

* Always-on passive listening
* Accurate Indian English recognition
* Noise-resistant
* Lightweight (~36 MB model)

Speak naturally and Buddy listens instantly.

---

## 🗣️ **3. Voice Output (Text-to-Speech)**

**Tools Used:**
✔ `Piper TTS` (Fast, GPU/CPU optimized)
✔ `playsound`

Features:

* Natural human-like voice
* Very low latency
* Completely offline
* Supports many voice models

Buddy sounds real and responsive.

---

## 🌐 **4. Online Search (DuckDuckGo API)**

When user says:

```
"search <query>"
"google <query>"
```

Buddy performs online search using:

* DuckDuckGo Instant Answer API 
* Returns clean text results
* Works even on low bandwidth

---

## 🪟 **5. Windows App & System Controller**

Buddy can open, launch, or control your PC.

### ✔ Open ANY PC App

Examples:

```
"open chrome"
"open spotify"
"open vs code"
"open epic games"
"open calculator"
```

Even non-typical apps:

```
"open bluestacks"
"open obs studio"
```

### ✔ Control System

```
shutdown
restart
sleep
```

### ✔ Open Websites

```
open youtube
open google
open github
```

---

## 💻 **6. Interactive Desktop GUI**

**Tools Used:**
✔ `tkinter`
✔ `ScrolledText`

GUI includes:

* Real-time chat viewer
* Live voice logs
* Clean, minimal interface
* Allows seamless voice + text interaction

---

# 🔧 **Tech Stack Overview**

| Component              | Tool / Model Used                 |
| ---------------------- | --------------------------------- |
| **Local LLM**          | Ollama + llama3.2:1b              |
| **Speech Recognition** | Vosk STT                          |
| **Audio Input**        | SoundDevice                       |
| **Text-to-Speech**     | Piper TTS                         |
| **Voice Playback**     | Playsound                         |
| **Online Search**      | DuckDuckGo Instant API            |
| **GUI Framework**      | Tkinter                           |
| **Windows Control**    | Python subprocess, os, webbrowser |
| **Python Version**     | 3.10+                  |



---

# ⚙️ **How Buddy Works (Flow Diagram)**

### 🎤 User Speaks →

### 🧠 Vosk STT Converts Speech →

### 🤖 Buddy Processes Intent

→ if command → Windows controller
→ if search → DuckDuckGo API
→ if chat → Local LLM

### 🗣️ Piper TTS Speaks Reply →

### 👤 GUI Displays Response

Everything happens smoothly and in real-time.

---

# 🏎️ **Performance (8GB RAM Compatible)**

Buddy is optimized for low-end devices:

* Uses only **300–500MB RAM**
* Runs fully local LLM
* No GPU required
* Piper TTS runs in <0.2 sec
* Vosk STT uses <50MB
* Extremely fast and responsive

Perfect for:

* Normal laptops
* Old desktops
* Portable installations

---

# 🔐 **Privacy & Security**

✔ Completely offline
✔ No server
✔ No cloud storage
✔ No data export
✔ Mic audio stays on your PC

Buddy is your truly private AI.

---

# 🌟 **Why Buddy is Different**

* Doesn’t rely on cloud APIs
* Extremely fast even on low hardware
* Real Windows OS control
* Offline + online hybrid
* Modular code — easy to extend
* Supports custom TTS voices
* Works like Jarvis but locally
* You can upgrade model anytime

---



# ❤️ **Credits**

* Local LLM — **Ollama**
* Offline Speech Recognition — **Vosk**
* Text-to-Speech — **Piper**
* GUI & Control — **Python**
* Online Search — **DuckDuckGo**


---

# 🎉 **Final Note**

Buddy is not just a project — it’s a **fully personal AI system** designed to work on normal hardware with absolute privacy.
You can keep extending it, upgrade models, add avatars, or turn it into a full desktop AI.
                                                                                          
---
