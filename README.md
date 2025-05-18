# 🎙️ Local Text-to-Speech System with Voice Cloning

This project implements a local, high-performance Text-to-Speech (TTS) system using [Coqui's XTTS v2](https://github.com/coqui-ai/TTS), capable of generating speech in multiple languages while cloning the voice of any speaker from a short audio sample. It also features a clean and interactive user interface powered by [Gradio](https://gradio.app/).

---

## 🚀 Features

- ✅ **Multilingual TTS** (supports FR, EN, DE, ES, etc.)
- 🧠 **Voice cloning** from a 5–15s `.wav` sample
- 🎧 **Audio output** saved as `.wav` (16kHz mono)
- 🌐 **Local-first** deployment — no cloud required
- 🖥️ Gradio UI for testing + real-time playback
- 📦 Ready for GitHub & deployment (clean structure)

---

## 🗂️ Project Structure
text-to-speech-project/
│
├── app/
│ ├── synthesize.py # Core XTTS logic
│ └── interface.py # Gradio app logic
│
├── static/
│ └── output.wav # Output audio file
│
├── data/
│ └── sample_voice.wav # Speaker reference file (10–15s)
│
├── run.py # Entry point to launch Gradio
├── requirements.txt # Pinned dependencies
├── .gitignore
└── README.md # You're reading it 😉

---

## 🧪 How to Use

### 1. Install Python 3.9 (required)

```bash
brew install python@3.9

### 2. Clone the repo and set up your environment
git clone https://github.com/YOUR_USERNAME/text-to-speech-project.git
cd text-to-speech-project

python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 3. Launch the app
python run.py



