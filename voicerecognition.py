import speech_recognition as sr
import pyttsx3
import gtts as gt
import os
import requests
import playsound



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty('voice', voices[6].id) #6 is good, 9 sounds indian

engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.5)
            voice = listener.listen(source)

            text = listener.recognize_google(voice)
            text = text.lower()
            print(text)
            
            if text.isnumeric():
                response = requests.get(f"https://api-thirukkural.vercel.app/api?num={text}")
                apidict = response.json()
                print(response.json())

                verse = apidict['line1'] + " " + apidict['line2']

                # engine.say(apidict['line1'])
                tts = gt.gTTS(text = verse, lang = "ta")

                tts.save("kuralexample.mp3")
                playsound.playsound("kuralexample.mp3")
                # os.system("kuralexample.mp3")
                #tts.write_to_fp("kuralexample.mp3")
                # os.remove(filename)
            else:
                print(f"Recognized {text}")
    except:
    #     print("Exception Reached")
        listener = sr.Recognizer()
        


