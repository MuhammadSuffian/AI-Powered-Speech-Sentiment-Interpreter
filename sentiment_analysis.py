import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
import os
import tempfile
st.set_page_config(page_title="Voice Sentiment Analyzer", page_icon="🎙️",
                      menu_items={
        'About': (
            "A Streamlit web app that lets you upload or record audio, convert it to text using Google Speech Recognition, and analyze the sentiment of the transcribed text using TextBlob.\n\n"
            "Developer:\n\n"
            "• M. Suffian Tafoor\n\n"
        )
    }
)
st.title("🎙️ Voice Sentiment Analyzer")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["Upload Audio", "Record Live Audio"])

with tab1:
    uploaded_file = st.file_uploader("Upload an audio file (WAV/MP3)", type=["wav", "mp3"])

    if uploaded_file:
        st.audio(uploaded_file)

        # Save uploaded file temporarily
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.read())

        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile("temp_audio.wav")

        with audio_file as source:
            st.info("Converting speech to text...")
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                st.success("Transcription:")
                st.write(text)

                # Sentiment analysis
                blob = TextBlob(text)
                sentiment = blob.sentiment.polarity
                sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
                
                st.subheader("Sentiment Analysis Result")
                st.metric(label="Sentiment", value=sentiment_label, delta=f"{sentiment:.2f}")

            except sr.UnknownValueError:
                st.error("Could not understand audio.")
            except sr.RequestError:
                st.error("Could not request results from the speech recognition service.")

with tab2:
    st.subheader("Record Audio Live")
    st.write("Click the button below to record audio from your microphone:")
    
    # Using Streamlit's audio input component
    audio_bytes = st.audio_input("Click to record")
    
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        
        # Save the recorded audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            # Read the content before writing - this fixes the bytes-like object issue
            audio_content = audio_bytes.read()
            tmp_file.write(audio_content)
            temp_filename = tmp_file.name
        
        try:
            # Process the recorded audio
            recognizer = sr.Recognizer()
            with sr.AudioFile(temp_filename) as source:
                st.info("Converting speech to text...")
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data)
                    st.success("Transcription:")
                    st.write(text)

                    # Sentiment analysis
                    blob = TextBlob(text)
                    sentiment = blob.sentiment.polarity
                    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
                    
                    st.subheader("Sentiment Analysis Result")
                    st.metric(label="Sentiment", value=sentiment_label, delta=f"{sentiment:.2f}")

                except sr.UnknownValueError:
                    st.error("Could not understand audio.")
                except sr.RequestError:
                    st.error("Could not request results from the speech recognition service.")
        finally:
            # Clean up temporary file
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
