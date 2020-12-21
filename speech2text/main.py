import speech_recognition as sr
import time

def record():
    recognizer = sr.Recognizer()
    print("Adjusting noise ")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while True:
            recorded_audio = recognizer.listen(source, timeout=5)
            try:
                text = recognizer.recognize_google(
                        recorded_audio, 
                        language="pt-BR"
                    )
                return text
            except Exception as ex:
                print(ex)