from pydub import AudioSegment
import speech_recognition as sr
import logging
import time

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the MP3 file and convert it to WAV format
wav_file = "../video2audio/output_audio.wav"

# Initialize the recognizer
recognizer = sr.Recognizer()

start_time = time.time()
logger.info('[Start time]: %d' % start_time)

# Load the WAV file for speech recognition
with sr.AudioFile(wav_file) as source:
    audio_data = recognizer.record(source)
    audio_time = time.time()
    logger.info('[Audio time]: %d' % audio_time)
    logger.info('Load audio file complete in %d s' % (audio_time - start_time))

# Recognize the speech
try:
    text = recognizer.recognize_google(audio_data, language="zh-CN")
    logger.info('Speech to text complete in %d s' % (time.time() - audio_time))
    print(text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))