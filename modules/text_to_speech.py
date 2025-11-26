import subprocess
import tempfile
import os
from playsound import playsound

PIPER_PATH = r"d:\Buddy\models\piper\piper.exe"          
VOICE_PATH = r"d:\Buddy\models\piper\voices\en-us-lessac-medium.onnx"  

def speak(text):
    """
    Convert text to speech using Piper + play audio via playsound.
    No simpleaudio, no build tools needed.
    """

   
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
        wav_path = temp_wav.name

    # Run Piper command to generate speech
    command = [
        PIPER_PATH,
        "--model", VOICE_PATH,
        "--output_file", wav_path
    ]

    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        process.stdin.write(text.encode("utf-8"))
        process.stdin.close()
        process.wait()

    except Exception as e:
        print(f"[ERROR] Piper failed: {e}")
        return

    # Play generated WAV using playsound
    try:
        playsound(wav_path)
    except Exception as e:
        print(f"[ERROR] Could not play audio: {e}")
    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)  # Clean temporary file
