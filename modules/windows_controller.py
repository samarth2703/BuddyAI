import os
import webbrowser
import subprocess

class WindowsController:

    def open_app(self, app_name):
        app_name = app_name.lower()

        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "wordpad": "write.exe",
            "cmd": "cmd.exe",
            "powershell": "powershell.exe",
            "explorer": "explorer.exe",
            "task manager": "taskmgr.exe"
        }

        for key in apps:
            if key in app_name:
                try:
                    subprocess.Popen(apps[key])
                    return f"Opening {key}."
                except:
                    return f"Unable to open {key}."
        return None

    def open_website(self, text):
        text = text.lower()

        sites = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "gmail": "https://mail.google.com",
            "github": "https://github.com",
            "chatgpt": "https://chat.openai.com"
        }

        for key in sites:
            if key in text:
                webbrowser.open(sites[key])
                return f"Opening {key}."
        return None

    def system_actions(self, text):
        text = text.lower()

        if "shutdown" in text:
            os.system("shutdown /s /t 3")
            return "Shutting down system."

        if "restart" in text:
            os.system("shutdown /r /t 3")
            return "Restarting system."

        if "sleep" in text:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return "Sleeping."
        return None


# Function used by main.py
controller = WindowsController()

def handle_windows_action(text):
    return (
        controller.open_app(text)
        or controller.open_website(text)
        or controller.system_actions(text)
    )
