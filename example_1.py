from email.mime import audio
import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:

    print("SPEAK...")
    audio = r.listen(source)
text_audio = r.recognize_google(audio)
print(text_audio.capitalize(), ".")
