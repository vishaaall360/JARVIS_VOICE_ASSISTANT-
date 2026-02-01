from assistant.speech import take_command
from assistant.voice import speak
from assistant.commands import run_command

speak("Jarvis is running. Say hey jarvis to activate.")

while True:
    command = take_command()

    if not command:
        continue

    if "hey jarvis" in command:
        speak("Yes, I am listening")

        command = take_command()

        if "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        run_command(command)
