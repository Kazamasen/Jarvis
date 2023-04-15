import pyttsx3
import datetime
import speech_recognition as rec
import wikipedia
import os
import webbrowser
#import section complete

Ai = pyttsx3.init('sapi5')
voices = Ai.getProperty('voices')
Ai.setProperty("voice", voices[1].id)
def speak(audio):
    Ai.say(audio)
    Ai.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning, everyone")
        speak("Good morning everyone")
    elif hour >= 12 and hour < 18:
        print("Good afternoon, everyone")
        speak("Good afternoon everyone")
    else:
        print("Good Evening, everyone")
        speak("Good Evening everyone")
    print("My name is Kally and I am here to help you. Just ask")
    speak("My name is kally and i am here to help you. Just ask")


def takecom():
    r = rec.Recognizer()
    with rec.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.phrase_threshold = 0.2
        r.operation_timeout = 2
        audio = r.listen(source)
    
    try:
        print("Recognition......")
        quest = r.recognize_google(audio, language= "en-in")#same engine used in phones
        print("User said: ", quest)
    except:
        print("Not audiuble. Plz try once more")
        speak("Not audiuble. Plz try once more")
        return "None"
    return quest


if __name__ == "__main__":
    wishme()
    while(True):
        quest = takecom().lower()
        #tasks performing
        if "wikipedia" in quest:
            speak("Searching Wikipedia......")
            quest = quest.replace("wikipedia", "")
            res = wikipedia.summary(quest, sentences = 3)
            speak("Wikipedia Says That")
            print(res)
            speak(res)
        elif "youtube" in quest:
            print("Opening...")
            speak("opening")
            webbrowser.open("https://www.youtube.com")
        elif "google" in quest:
            print("Opening...")
            speak("opening")
            webbrowser.open("https://www.google.com")
        elif "github" in quest:
            print("Opening...")
            speak("opening")
            webbrowser.open("https://www.github.com")
        elif "instagram" in quest:
            print("Opening...")
            speak("opening")
            webbrowser.open("https://www.instagram.com")
        elif "facebook" in quest:
            print("Opening...")
            speak("opening")
            webbrowser.open("https://www.facebook.com")
        elif "play music" in quest:
            print("Opening...")
            speak("opening") 
            music_d = "C:\\Users\\Abc\\OneDrive\\Documents\\Rockstar Games\\GTA V\\User Music"
            songs = os.listdir(music_d)
            os.startfile(os.path.join(music_d, songs[0]))
        elif "time" in quest:
            Time = datetime.datetime.now().strftime("%H, %M, %S")
            print(Time)
            speak(f"Sir, the time is{Time}")
        elif "thank you" or "thankyou" in quest:
            print("I am really please by helping You!!!!!")
            speak("I am really please by helping You!!!!!")
            exit()