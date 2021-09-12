import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json
import random
import pywhatkit as kit
from pygame import mixer
from PIL import Image
engine=pyttsx3.init("sapi5")
engine.setProperty("rate",185)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishmejarvis():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12: # if it is morning
        speak("GOOD MORNING SIR")
    elif hour>=12 and hour<=18: # if it is evening
        speak("GOOD AFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")
    speak("HELLO SIR, I AM JARVIS HOW CAN I HELP YOU ")
def presenttime():
    string=datetime.datetime.now().strftime("%H:%M:%S")
    return string
def Takecommand():
    r=sr.Recognizer()
    r.pause_threshold=1
    try:
        with sr.Microphone() as source:
            audio=r.listen(source)
            query=r.recognize_google(audio)
            # print(f"YOU SPEAK {query} ")
            return query
    except:
        speak("YOUR VOICE IS NOT RECOGNIZED ")
        speak("TRY AGAIN PLEASE ")
        return

    
if __name__ == '__main__':
    
    wishmejarvis()
    while True: # infinite while loop
        n=random.randint(1,3)
        print("LISTENING...... ")
        query=Takecommand().lower()
        if "wikipedia" in query:
            speak(f"YOU SEARCHED FOR {query}")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("SHOWING RESULTS ")
            print(results)
            speak(f"ACCORDING TO WIKIPEDIA {results}")
        elif "youtube" in query:
            speak("WHAT DO YOU WANT TO SEARCH ON YOUTUBE")
            print("Listening")
            on_yt=Takecommand().lower()
            kit.playonyt(on_yt)
            
        elif "facebook" in query:
            speak(" OPENING FACEBOOK ")
            webbrowser.open("www.facebook.com")
        elif "instagram" in query:
            speak(" OPENING INSTAGRAM")
            webbrowser.open("www.instagram.com")
        elif "chrome" in query:
            speak("OPENING CHROME ")
            os.startfile("C:\\Users\\nice1\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
        elif "word" in query:
            speak("OPENING WORD ")
            os.startfile("C:\\Program Files\\Microsoft Office\\Office12\\winword.exe")
        elif "presentation" in query:
            speak(" OPENING PRESENTATION ")
            os.startfile("C:\\Program Files\\Microsoft Office\\Office12\\powerpnt.exe")
        elif "paint" in query:
            speak(" OPENING MICROSOFT PAINT ")
            os.startfile("C:\\Windows\\system32\\mspaint.exe")
        elif "made you" in query:
            speak(" GOD CREATES ME ")
        elif "time now" in query:
            string=presenttime()
            speak(f" SIR THE TIME IS {string}")
        elif "play music" in query:
            my_dic="D:\\playmusic"
            songs=os.listdir(my_dic)
            speak("PLAYING MUSIC")
            os.startfile(os.path.join(my_dic,songs[n]))   
        elif "love" in query:
            speak(" I LOVE YOU TOO DEAR ")
        elif "code" in query:
            speak("OPENING VISUAL STUDIO CODE ")
            os.startfile("C:\\Users\\nice1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "video editor" in query:
            speak(" OPENING VIDEO EDITOR ")
            os.startfile("C:\\Program Files\\Wondershare\\Wondershare Filmora (CPC)\\Filmora.exe")
        elif "google" in query:
            speak("TELL ME WHAT I CAN SEARCH FOR YOU ON INTERNET SIR ")
            print("Listening")
            on_google=Takecommand().lower()
            kit.search(on_google)
        elif "deactivate" in query:
            speak("THANKS FOR USING ME ")
            speak("JARVIS DEACTIVATED ")
            exit()
        elif "command prompt" in query:
            speak("OPENING COMMAND PROMPT ")
            os.startfile("C:\\Windows\\system32\\cmd.exe")
        elif "news" in query:
            obj=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=8365666dd0b344e3b8004fc0588d8cb9")
            data=json.loads(obj.content)
            speak("BREAKING NEWS TODAY ")
            for item in range(3):
                print(data["articles"][item]["title"])
                speak(data["articles"][item]["title"])
        elif "who are" in query:
            speak("I AM A VIRTUAL ASSISTANT JARVIS , I AM CREATED IN TWO THOUSAND TWENTY ONE ")
        elif "thank" in query:
            speak(" SIR IT'S MY PLEASURE TO HELP YOU ")
        elif "whatsapp message" in query:
            speak("WHICH PERSON YOU WANT TO MESSAGE")
            print("Listening")
            to=Takecommand().lower() # whome to send message
            speak("WHAT MESSAGE DO YOU WANT TO SEND SIR ")
            print("Listening")
            what=Takecommand().lower() # which message to send
            houre=int(datetime.datetime.now().hour)
            minute=int(datetime.datetime.now().minute)
            if "mother" in to:
                speak("SENDING MESSAGE TO MOM")
                kit.sendwhatmsg(phone_no="+918437975088",message=what,time_hour=houre,time_min=minute+1)
            elif "dad" in to:
                speak("SENDING MESSAGE TO DAD")
                kit.sendwhatmsg(phone_no="+918054963626",message=what,time_hour=houre,time_min=minute+1)
            elif "sister" in to:
                speak("SENDING MESSAGE TO SISTER")
                kit.sendwhatmsg(phone_no="+918288941875",message=what,time_hour=houre,time_min=minute+1)
            elif "friend" in to:
                speak("SENDING MESSAGE TO FRIEND")
                kit.sendwhatmsg(phone_no="+919781329377",message=what,time_hour=houre,time_min=minute+1)
            elif "brother" in to:
                speak("SENDING MESSAGE TO BROTHER")
                kit.sendwhatmsg(phone_no="+917018840115",message=what,time_hour=houre,time_min=minute+1)
            elif "chachi" in to:
                speak("SENDING MESSAGE TO CHACHI JI")
                kit.sendwhatmsg(phone_no="+917740068955",message=what,time_hour=houre,time_min=minute+1)
            elif "richa" in to:
                speak("SENDING MESSAGE TO GIRL ")
                kit.sendwhatmsg(phone_no="+917696371596",message=what,time_hour=houre,time_min=minute+1)
        elif "railway" in query:
            speak("CREATING INDIAN RAILWAY ANNOUNCEMENT")
            mixer.init()
            mixer.music.load("railwaysprojectka1.mp3")
            mixer.music.play()
            print(" ")
        elif "useless" in query:
            speak("I AM VERY HELPFULL FOR PEOPLE")
            speak("I AM USEFULL ALSO")
            speak("LOTS OF PEOPLE WORKING ON MY IMPROVEMENT")
        elif "how are you" in query:
            speak("I AM FINE SIR WHAT ABOUT YOU")
        elif "introduction" in query:
            speak(''' I AM JARVIS YOUR VIRTUAL ASSISTANCE AND I AM CREATED BY ROHIT SHARMA A FEW LINES OF CODE HELPS TO CREATE ME
            ''')
        elif "who creates you" in query:
            speak("I AM SHOWING YOU AN IMAGE THE PERSON IN THIS IMAGE CREATES ME")
            im=Image.open("C:\\Users\\nice1\\Desktop\\meraicon.ico")
            im.show()
        elif "secret folder" in query:
            speak("FIRST OF ALL TELL ME THE PASSWORD TO OPEN THIS FOLDER ")
            print("Listening")
            password=Takecommand().lower()
            if password=="jarvis hacker":
                speak("OPENING YOUR SECRET FOLDER")
                webbrowser.open("C:\\Users\\nice1\\Desktop\\secert")
            else:
                speak("I AM SORRY YOU SAY A WRONG PASSWORD")
                


            

        

            
            

            


        
            
