import threading
import tkinter as tk
import math
import time

from assistant.speech import take_command
from assistant.voice import speak
from assistant.commands import run_command

listening = False
pulse = 0


# ---------------- JARVIS LOOP ---------------- #
def jarvis_loop():
    global listening
    update_status("LISTENING")
    speak("Jarvis online")

    while listening:
        command = take_command()
        if not command:
            continue

        if "stop listening" in command:
            stop_jarvis()
            break

        run_command(command)


# ---------------- BUTTON ACTIONS ---------------- #
def start_jarvis():
    global listening
    if not listening:
        listening = True
        threading.Thread(target=jarvis_loop, daemon=True).start()


def stop_jarvis():
    global listening
    listening = False
    update_status("IDLE")
    speak("Jarvis offline")


def update_status(text):
    status_label.config(text=text)


# ---------------- HUD ANIMATION ---------------- #
def animate_arc():
    global pulse
    canvas.delete("pulse")

    r = 80 + int(10 * math.sin(pulse))
    pulse += 0.2

    canvas.create_oval(
        150 - r, 150 - r,
        150 + r, 150 + r,
        outline="#00FFF7",
        width=2,
        tags="pulse"
    )

    root.after(50, animate_arc)


# ---------------- GUI SETUP ---------------- #
root = tk.Tk()
root.title("JARVIS HUD")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#050B14")

canvas = tk.Canvas(root, width=300, height=300, bg="#050B14", highlightthickness=0)
canvas.pack(pady=20)

# ARC REACTOR CIRCLES
canvas.create_oval(50, 50, 250, 250, outline="#00FFF7", width=3)
canvas.create_oval(70, 70, 230, 230, outline="#FF3B3B", width=2)
canvas.create_oval(95, 95, 205, 205, outline="#00FFF7", width=2)

canvas.create_text(
    150, 150,
    text="JARVIS",
    fill="#00FFF7",
    font=("Orbitron", 18, "bold")
)

# STATUS
status_label = tk.Label(
    root,
    text="IDLE",
    font=("Orbitron", 12),
    fg="#00FFF7",
    bg="#050B14"
)
status_label.pack(pady=10)

# BUTTONS
btn_frame = tk.Frame(root, bg="#050B14")
btn_frame.pack(pady=20)

start_btn = tk.Button(
    btn_frame,
    text="▶ ACTIVATE",
    font=("Orbitron", 11),
    width=14,
    bg="#00FFF7",
    fg="black",
    bd=0,
    command=start_jarvis
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="⏹ DEACTIVATE",
    font=("Orbitron", 11),
    width=14,
    bg="#FF3B3B",
    fg="white",
    bd=0,
    command=stop_jarvis
)
stop_btn.grid(row=0, column=1, padx=10)

# FOOTER
footer = tk.Label(
    root,
    text="VOICE INTERFACE ONLINE",
    font=("Orbitron", 9),
    fg="#888888",
    bg="#050B14"
)
footer.pack(side="bottom", pady=15)

animate_arc()
root.mainloop()
