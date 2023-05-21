from playsound import playsound
from gtts import gTTS
import os

speak = gTTS(text='I am Vietnamese', lang='en', slow=False)
speak.save('captured_voice.mp3')
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')