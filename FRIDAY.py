import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id) # chon giong nu

def speak(audio):
    print('F.R.I.D.A.Y : ')
    friday.say(audio)
    friday.runAndWait()
# speak("hello youtube")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    print(Time)
    speak(Time)
#time()

def Welcome():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning sir")
        print("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
        print("Good Afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good Night sir")
        print("Good Night sir")
    speak("how can I help you ?")
# Welcome()

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2 # dung 2s trc khi nghe lenh ms
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio,language='en')
        print("Quang Nguyen :"+query)
    except sr.UnknownValueError:
        print("Please repeat our typing command ")
        query = str(input('Your order is : '))
    return query
if __name__ == "__main__":
    Welcome()
    while(True):
        query = command().lower()   # lay lenh va chuyen thanh dang ko viet hoa cho may de nhan dien
        if "google" in query:
            speak("What should I search boss ?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("What should I search boss ?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video " in query:
            video = r"C:\Users\Nguyen Van Huy\Videos\MyVideo\NuiTram2019.mp4"
            os.startfile(video)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("friday is quitting sir. Good bye boss")
            quit()