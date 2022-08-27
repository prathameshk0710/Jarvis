from email import message
from http import server
from re import sub
import smtplib
from turtle import speed
import pyttsx3
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import yagmail
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        speak("Good morning, Prathamesh")
    elif(hour >= 12 and hour < 16):
        speak("Good Afternoon, Prathamesh")
    elif(hour >= 16 and hour < 21):
        speak("Good evening, Prathamesh")
    elif(hour >= 21):
        speak("Good night, Prathamesh")

    speak("Myself Jarvis, How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said :- ", query)

    except Exception as e:
        print("say that again please...")
        return "None"

    return query


def youtube(query):
    song = query.replace('play', '')
    speak("playing" + song)
    print('playing, ' + song)
    pywhatkit.playonyt(song)


def sendEmail():

    speak('Whom do you want to send the E-mail?')
    Name = takeCommand().lower()
    receiver = email_list[Name]
    print(receiver)

    speak('What is the purpose of this mail?')
    subject = takeCommand().lower()

    speak('what is your message')
    message = takeCommand().lower()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pk.kondawale191111989@gmail.com', 'pk@prathamesh71816$$')
    server.sendmail('pk.kondawale191111989@gmail.com', receiver, message)
    print('done')

    # email = EmailMessage()
    # email['From'] = 'pk.kondawale191111989@gmail.com'
    # email['To'] = receiver
    # email['Subject'] = subject
    # email.set_content(message)
    # server.send_message(email)

    server.close()
    print('Mail sent')
    speak('Your mail has been sent successfully')

    speak('Do you want to send more email?')
    res = takeCommand().lower()

    if 'yes' in res:
        sendEmail()


email_list = {
    'myself': 'cp.kondawale786@gmail.com',
    'domain': 'kondawale_12013060@nitkkr.ac.in',
    'father': 'cg.kondawale@sbi.co.in'
}

if __name__ == '__main__':
    greet()

    while True:
        query = takeCommand().lower()
        query = query.replace("jarvis", "")

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(time)
            speak('Sir, The time is ' + time)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            # url = 'https://www.youtube.com/'
            # webbrowser.register('chrome', None)
            # webbrowser.BackgroundBrowser(
            #     'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            # webbrowser.get('chrome').open('youtube.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play music from directory' in query:
            music = 'D:\\songs'
            song = os.listdir(music)
            play = random.choice(song)
            os.startfile(os.path.join(music, play))

        elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            youtube(query)

        elif 'send email' in query:
            sendEmail()

        elif 'exit' in query:
            speak('Hope you had a great time.')
            exit()
