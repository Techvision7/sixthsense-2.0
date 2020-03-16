import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
from camera import camera
from face_recognizer import recognise


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! sir')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! sir')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening! Sir')
greetMe()
#speak('hey BOSS   How may I help you?')
#speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print('User: ' + command + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        command = str(input('Command: '))

    return command
        

if __name__ == '__main__':

    while True:
    
        command = myCommand();
        command = command.lower()
        
        if 'Destiny' in command and 'open youtube' in command:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'Destiny' in command and 'open google' in command:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'Destiny' in command and 'open gmail' in command:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'Destiny' in command and "what\'s up" in command or 'how are you' in command:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'Destiny' in command and 'email' in command:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif command and 'abort' in command or 'stop' in command:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in command and 'Destiny' in command:
            speak('Hello Sir')
            speak(greetMe())
                                    
        elif 'Destiny' in command and 'play music' in command:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            
        elif 'Destiny' in command and 'Turn on gesture mode' in command:
            speak('Turning on gesture mode')

        elif 'Destiny' in command and 'Recognise faces' in command or 'Recognise faces' in command:
            speak('Recognising faces')
            recognise()

        else:
            if 'Destiny' not in command:
                speak("Are you talking to me if yes please say Destiny in front of the command")