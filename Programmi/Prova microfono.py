import speech_recognition as sr

# obtain audio from the Microphone
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Parla")
    audio=r.listen(source)

try:
    print("Transcription"+rrecognize_google(audio))
except sr.UnknownValueError:
    print("NO")
except sr.RequestError as e:
    print("Cannot obtain results; {0}",format(e))
