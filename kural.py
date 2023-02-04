import gtts as gt
import requests
import playsound
import os

def kuralgrabber(kuralnum):
    if kuralnum.isnumeric() and int(kuralnum) >= 1 and int(kuralnum) <= 1330:
        response = requests.get(f"https://api-thirukkural.vercel.app/api?num={kuralnum}")
        apidict = response.json()
        # print(response.json())

        verse = apidict['line1'] + " " + apidict['line2']

        # engine.say(apidict['line1'])
        # mp3_fp = BytesIO()
        tts = gt.gTTS(text = verse, lang = "ta")
        tts2 = gt.gTTS(text = apidict['tam_exp'], lang = "ta")
        # tts.write_to_fp(mp3_fp)
        tts.save(os.getcwd() + "kuralexample.mp3")
        print(os.getcwd() + "kuralexample.mp3")
        playsound.playsound(os.getcwd() + "kuralexample.mp3")
        tts2.save(os.getcwd() + "englexample.mp3")
        playsound.playsound(os.getcwd() + "englexample.mp3")

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
    verse = apidict['line1'] + "\n" + apidict['line2']
    return [apidict['line1'], apidict['line2'], apidict['tam_exp']]