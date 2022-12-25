import gtts as gt
import os
import requests
import playsound

def kuralgrabber(kuralnum):
    if kuralnum.isnumeric() and int(kuralnum) >= 1 and int(kuralnum) <= 1330:
        response = requests.get(f"https://api-thirukkural.vercel.app/api?num={kuralnum}")
        apidict = response.json()
        print(response.json())

        verse = apidict['line1'] + " " + apidict['line2']

        # engine.say(apidict['line1'])
        tts = gt.gTTS(text = verse, lang = "ta")

        tts.save("kuralexample.mp3")
        playsound.playsound("kuralexample.mp3")

        return [verse, apidict['eng_exp']]
        # os.system("kuralexample.mp3")
        #tts.write_to_fp("kuralexample.mp3")
        # os.remove(filename)
    else:
        print("incorrect value")
        return

def kuraldefinition(kuralnum):
    response = requests.get(f"https://api-thirukkural.vercel.app/api?num={kuralnum}")
    apidict = response.json()
    verse = apidict['line1'] + " " + apidict['line2']
    return [verse, apidict['eng_exp']]