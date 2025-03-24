## Audio Translator App
### Overview
This is a simple Streamlit web application that allows users to upload an audio file, select a target language (Hindi, Telugu, Kannada), and then translates and plays the audio within the app.

### Features
Upload an audio file in WAV or MP3 format.
Select the target language for translation (Hindi, Telugu, Kannada).
Translate the uploaded audio to the selected language.
Play the translated audio within the app.

### Prerequisites
Python 3.6 or later
Install dependencies using pip install -r requirements.txt

### How to Run
1. Clone this repository:
git clone https://github.com/Anjureddyk/Audio_Translator_Using_gtts.git

2. Navigate to the project directory:
cd audio-translator-app

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

### Usage
Upload an audio file using the provided file uploader.
Select the target language for translation (Hindi, Telugu, Kannada).
Click the "Translate" button to perform the translation.
Once translated, the "Play Translated Audio" button will appear.
Click the "Play Translated Audio" button to listen to the translated audio.

### Dependencies
Streamlit
SpeechRecognition
googletrans==4.0.0
gtts

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
