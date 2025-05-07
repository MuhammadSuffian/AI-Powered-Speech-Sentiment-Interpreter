# 🎙️ AI-Powered Speech Sentiment Interpreter

A Streamlit web app that lets you **upload or record audio**, convert it to text using **Google Speech Recognition**, and analyze the **sentiment** of the transcribed text using **TextBlob**.

---

## 🚀 Features

- 🎧 **Upload Audio**: Supports `.wav` and `.mp3` files.
- 🎤 **Record Live Audio**: Record directly using your microphone via Streamlit’s `audio_input`.
- 📝 **Speech-to-Text**: Uses `speech_recognition` to transcribe audio.
- 💡 **Sentiment Analysis**: Detects whether the sentiment is **Positive**, **Negative**, or **Neutral** using `TextBlob`.
- 📊 **Interactive UI**: Displays transcription and sentiment results clearly in a responsive interface.
- ⚠️ **Error Handling**: Handles unknown speech and API errors gracefully.

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [pydub (optional)](https://github.com/jiaaro/pydub) 

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/voice-sentiment-analyzer.git
cd voice-sentiment-analyzer

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
