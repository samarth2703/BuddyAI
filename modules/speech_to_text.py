import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import threading


class SpeechToText:
    def __init__(self, model_path="models/vosk-model-small-en-in-0.4", rate=16000):
        self.model = Model(model_path)
        self.rate = rate
        self.q = queue.Queue()
        self.listening = False

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.q.put(bytes(indata))

    def start_listening(self, callback):
        """
        callback: function that receives recognized text
        """
        if self.listening:
            return
        
        self.listening = True

        def listen():
            rec = KaldiRecognizer(self.model, self.rate)

            with sd.RawInputStream(samplerate=self.rate, blocksize=8000,
                                   dtype='int16', channels=1, callback=self._callback):

                while self.listening:
                    data = self.q.get()
                    if rec.AcceptWaveform(data):
                        result = json.loads(rec.Result())
                        if "text" in result and result["text"].strip() != "":
                            callback(result["text"])
                    else:
                        partial = json.loads(rec.PartialResult())
                        # You can capture partial results here

        threading.Thread(target=listen, daemon=True).start()

    def stop_listening(self):
        self.listening = False
