import streamlit as st
import speech_recognition
import googletrans
import gtts
from io import BytesIO

# Function to recognize speech from an audio file
def recognize_speech_from_file(audio_file_path):
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.AudioFile(audio_file_path) as source:
        st.info("Processing audio file...")
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data, language="en")  # Assuming the input audio is in English
        return text
    except speech_recognition.UnknownValueError:
        st.warning("Speech recognition could not understand audio.")
        return None
    except speech_recognition.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to translate text to the selected language and save as an audio file
def translate_and_save(text, language, output_file_path="output.mp3"):
    translator = googletrans.Translator()
    translation = translator.translate(text, dest=language)
    
    converted_audio = gtts.gTTS(translation.text, lang=language)
    converted_audio.save(output_file_path)
    
    st.success(f"Translation saved as {output_file_path}")
    return output_file_path

# Streamlit app
def main():
    st.title("Audio Translator App")

    # Upload audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav', start_time=0)
        st.info("Audio file uploaded successfully!")

        # Language selection
        language = st.selectbox("Select language for translation", ["hi", "te", "kn"])

        # Translate button
        if st.button("Translate"):
            audio_file_path = "uploaded_audio.wav"
            uploaded_file.seek(0)
            with open(audio_file_path, "wb") as f:
                f.write(uploaded_file.read())

            recognized_text = recognize_speech_from_file(audio_file_path)

            if recognized_text:
                output_audio_file = translate_and_save(recognized_text, language)
                st.success("Translation complete!")
                st.button("Play Translated Audio", key="play_button", on_click=play_audio, args=(output_audio_file,))

# Function to play audio
def play_audio(output_audio_file):
    st.audio(output_audio_file, format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
