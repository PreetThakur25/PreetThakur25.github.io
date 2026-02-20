# Real-Time Speech-to-Text Transcriber

A lightweight, offline real-time speech recognition tool that transcribes microphone input instantly to text — no internet connection or cloud API required. Built with **Vosk** and **SoundDevice**.

---

## Overview

This project captures live audio from your microphone and converts it to text in real time using a locally bundled Vosk speech recognition model. Everything runs on-device, keeping your audio completely private.

---

## Features

- **100% Offline** — Uses a bundled Vosk model; no internet required
- **Real-Time Transcription** — Streams and recognizes speech continuously as you speak
- **Low Latency** — Processes audio in 8000-sample chunks at 16kHz for fast response
- **Lightweight** — Runs on CPU with minimal resources
- **Privacy-First** — Audio never leaves your machine

---

## Tech Stack

| Component | Technology |
|---|---|
| Speech Recognition | [Vosk](https://alphacephei.com/vosk/) |
| Audio Capture | [SoundDevice](https://python-sounddevice.readthedocs.io/) |
| Acoustic Model | `vosk-model-small-en-us-0.15` (English) |
| Language | Python 3.10+ |

---

## Project Structure

```
speech_to_text/
├── texter.py                        # Main real-time transcription script
└── vosk-model-small-en-us-0.15/    # Bundled offline speech model
```

---

## Prerequisites

- **Python 3.10+**
- A working **microphone**
- On Windows, you may need [PortAudio](http://www.portaudio.com/) (bundled with most SoundDevice installs via pip)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/speech_to_text.git
cd speech_to_text

# Create and activate a virtual environment
python -m venv ttsss
ttsss\Scripts\activate      # Windows
# source ttsss/bin/activate # macOS/Linux

# Install dependencies
pip install vosk sounddevice
```

> The Vosk small English model (`vosk-model-small-en-us-0.15`) is included in the repository.
> For other languages or larger/more accurate models, visit [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models).

---

## Usage

```bash
python texter.py
```

**Example output:**
```
Speak into the microphone...
Recognized: hello how are you
Recognized: this is a test of the speech recognition system
```

Speak clearly into your microphone. Recognized phrases are printed to the console as they are detected. Press `Ctrl+C` to stop.

---

## How It Works

1. `SoundDevice` opens a raw audio stream from your default microphone at 16kHz, mono, 16-bit PCM
2. Audio chunks are pushed into a thread-safe queue via a callback
3. `KaldiRecognizer` (from Vosk) processes each chunk against the bundled acoustic model
4. When a complete utterance is detected, the transcribed text is printed to the console

---

## Extending the Project

- **Change language** — Swap the model folder with any Vosk-supported language model
- **Higher accuracy** — Replace `vosk-model-small-en-us-0.15` with a larger model (e.g., `vosk-model-en-us-0.22`)
- **Pipe output** — Redirect recognized text to a file, a clipboard manager, or another application

---

## License

MIT License — free to use, modify, and distribute.
