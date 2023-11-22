import speech_recognition
import googletrans
import gtts
import playsound

# Function to recognize speech from an audio file
def recognize_speech_from_file(audio_file_path):
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.AudioFile(audio_file_path) as source:
        print("Processing audio file...")
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data, language="en")  # Assuming the input audio is in English
        return text
    except speech_recognition.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to translate text to Hindi and save as an audio file
def translate_and_save(text, output_file_path="output.mp3"):
    translator = googletrans.Translator()
    translation = translator.translate(text, dest="hi")
    
    converted_audio = gtts.gTTS(translation.text, lang='hi')
    converted_audio.save(output_file_path)
    
    print(f"Translation saved as {output_file_path}")

# Example usage
if __name__ == "__main__":
    input_audio_file = "audio1.wav"  # Change this to the path of your English audio file
    output_audio_file = "hello_hindi.mp3"  # Change this to the desired output file path
    
    recognized_text = recognize_speech_from_file(input_audio_file)
    
    if recognized_text:
        translate_and_save(recognized_text, output_audio_file)
        playsound.playsound(output_audio_file)
