from gtts import gTTs
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTs(text = "Hello please enter something in here", lang= language, slow=False)

sp.save(audio)
playsound(audio)