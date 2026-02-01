import datetime
import os
import wikipedia
import pyautogui
import time
from assistant.voice import speak

# Store pending critical action
pending_action = None

# Base folder for file creation
BASE_DIR = os.path.join(os.path.expanduser("~"), "JarvisFiles")
os.makedirs(BASE_DIR, exist_ok=True)


def run_command(command):
    global pending_action

    command = command.lower().strip()

    # 🕒 TIME
    if command == "time" or "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")

    # 🌐 OPEN APPS
    elif command == "open chrome":
        os.system("start chrome")
        speak("Opening Chrome")

    elif command == "open youtube":
        os.system("start https://www.youtube.com")
        speak("Opening YouTube")

    # 🎵 MEDIA (Spotify via media keys)
    elif command == "play song":
        os.system("start spotify")
        time.sleep(4)
        pyautogui.press("playpause")
        speak("Playing music")

    elif command == "pause":
        pyautogui.press("playpause")
        speak("Paused")

    elif command == "resume":
        pyautogui.press("playpause")
        speak("Resumed")

    # 🔊 VOLUME
    elif command == "volume up":
        pyautogui.press("volumeup")
        speak("Volume increased")

    elif command == "volume down":
        pyautogui.press("volumedown")
        speak("Volume decreased")

    elif command == "mute":
        pyautogui.press("volumemute")
        speak("Muted")

    # 📁 FILE CREATION (FIXED)
    elif command == "create file":
        file_path = os.path.join(BASE_DIR, "new_file.txt")
        with open(file_path, "w") as f:
            f.write("Created by Jarvis")
        speak("File created successfully")
        speak("You can find it in the JarvisFiles folder")

    # 💻 SHUTDOWN / RESTART (VOICE CONFIRMATION)
    elif command == "shutdown":
        pending_action = "shutdown"
        speak("Are you sure you want to shut down? Say confirm or cancel.")

    elif command == "restart":
        pending_action = "restart"
        speak("Are you sure you want to restart? Say confirm or cancel.")

    elif command == "confirm":
        if pending_action == "shutdown":
            speak("Shutting down system")
            os.system("shutdown /s /t 5")
        elif pending_action == "restart":
            speak("Restarting system")
            os.system("shutdown /r /t 5")
        pending_action = None

    elif command == "cancel":
        speak("Action cancelled")
        pending_action = None

    # 📚 WIKIPEDIA
    elif command.startswith("who is") or command.startswith("what is"):
        try:
            info = wikipedia.summary(command, sentences=2)
            speak(info)
        except:
            speak("Sorry, I could not find information")

    else:
        speak("Command not recognized")
