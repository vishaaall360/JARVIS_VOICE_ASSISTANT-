# 🎙️ Jarvis – Voice Controlled Desktop Assistant

Jarvis is a **Python-based voice-controlled desktop assistant** inspired by Iron Man’s JARVIS.  
It allows users to **control their laptop entirely using voice commands**, including system operations, file management, media playback, Spotify control, and AI-powered responses — all through a futuristic GUI.

---

## 🚀 Features

### 🎤 Voice Control
- Wake word activation (e.g., *“Hey Jarvis”*)
- Hands-free laptop control
- Accurate speech recognition with noise handling

### 🖥️ System Control
- Get current time
- Shutdown & restart (with voice confirmation)
- Volume up / down / mute
- Media play, pause, resume

### 📁 File & Folder Operations
- Create files using voice
- Open Downloads & Documents folders
- Files saved in a dedicated `JarvisFiles` directory

### 🎵 Spotify Integration
- Play music directly on Spotify Desktop
- Pause, resume, next, previous song
- Optional Spotify API integration for advanced control

### 🌐 Application Control
- Open Chrome
- Open YouTube
- Open system applications

### 🧠 AI Capabilities
- AI-powered answers using OpenAI API
- Handles natural language queries like:
  - *“What is artificial intelligence?”*
  - *“Who is Elon Musk?”*

### 🧩 Graphical User Interface
- Futuristic **Iron-Man HUD–style GUI**
- Start / Stop listening buttons
- Animated arc-reactor style UI
- Non-blocking threaded execution

---

## 🛠️ Technologies Used

- **Python 3.9+**
- SpeechRecognition
- pyttsx3 (Text-to-Speech)
- pyautogui
- Spotify API (Spotipy)
- OpenAI API
- Tkinter (GUI)
- Threading

---

## 📂 Project Structure

Jarvis-Voice-Assistant/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .env.example
│
├── assistant/
│ ├── init.py
│ ├── speech.py
│ ├── voice.py
│ ├── commands.py
│ ├── spotify_control.py
│ └── ai_chat.py
│
├── gui/
│ ├── init.py
│ └── app.py
│
├── config/
│ └── settings.py
│
├── docs/
│ ├── setup.md
│ ├── commands.md
│ ├── architecture.md
│ ├── faq.md
│ └── troubleshooting.md
│
├── logs/
│ └── jarvis.log
│
├── tests/
│ └── test_commands.py
│
└── assets/
└── screenshots/
└── gui.png

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

👨‍💻 Author

Vishaal S
B.E – Computer Science & Engineering (Cyber Security / AIML)
Passionate about AI, system automation, and intelligent assistants.
