from gtts import gTTS
import os
fx=gTTS("Ciao, come stai?",lang="it")
fx.save("Prova.mp3")
fx=gTTS("NOS4A2",lang="it")
fx.save("Prova1.mp3")

os.system("start Prova.mp3")

