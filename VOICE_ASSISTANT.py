#HAFSA AND DORAEMON A VOICE ASSISTANT USING PYTHON
import datetime
import time
from time import strftime
import pyaudio
import os
import subprocess
import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia

#The starts from here
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #without this command speak will not be audible to us so we nned to write this

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif  hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else :
        speak("Good Evening Sir!")
    assname =("HAFSA")
    speak("I am HAFSA. Your Voice Assistant. How can I assist you Sir!")
    #speak(assname)

def takecommand():
    #It takes microphone ae input from user to print string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"You said: {query}\n")  #User query will be printed.
    
        except Exception as e:
          # print(e)    
          print("Say that again please...")   #Say that again will be printed in case of improper voice 
          return "None" #None string will be returned

        return query

if __name__ == '__main__':
    wishme()
    while True:
      query = takecommand().lower()

      #Logic for executing tasks based on query
      if 'wikipedia' in query:
          speak("Searching wikipedia sir\n")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences = 2)
          speak("According to wikipedia")
          print(results)
          speak(results)
  
      elif 'open youtube' in query:
          speak("Opening YouTube Sir\n")
          webbrowser.open("youtube.com")
  
      elif 'open google' in query:
          speak("Opening Google Sir\n")
          webbrowser.open("google.com")   
  
      elif 'play music' in query or 'play song' in query:
          speak("Playing music sir\n")
          music_dir = "C:\\Users\\siddi\\Music\\Background Audio"
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[2]))  

      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          print(strTime)
          speak(f"Sir, The time is {strTime}")

      elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
          speak("A warm" +query)
          speak("How are you sir\n")
 
      elif 'will you be my girlfriend' in query or 'will you be my boyfriend' in query:  
          speak("I'm not sure about, may be you should give me some time sir\n")
  
      elif 'i love you' in query:
          speak("It's hard to understand because i am an voice assistant sir and I am Rod Single\n")  

      elif 'how are you' in query:
          speak("I am Fine , Thank you sir\n")
          speak("How are you, sir?")
 
      elif 'fine' in query:
          speak("I am happy to know that you are fine, sir\n")      
 
      elif 'change your name' in query:
          speak("What would you like to call me, sir\n")
          assname = takecommand()
          speak("Thank you sir for naming me")

      elif 'vs code' in query:
          speak("Opening vs code, sir\n")
          codepath = "C:\\Users\\siddi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)

      elif 'who made you' in query or 'developed'in query or 'designed' in query or 'programmed' in query or 'created' in query:
          speak("I have been designed, developed and created by, teja and siddiq\n")

      elif 'who i am' in query or 'who am i' in query:
          speak("I think your a human being sir\n")  

      elif 'joke' in query:
          speak(pyjokes.get_joke())

      elif 'search' in query or 'play' in query: 
          query = query.replace("search", "")
          query = query.replace("play", "")   
          speak("searching"+query)      
          webbrowser.open("google.com"+query)

      elif "don't listen" in query or 'stop listening' in query or 'stop listen' in query:
          speak("for how much time sir you need to stop listening me")
          a = int(takecommand())
          time.sleep(a)  
          print(a)
 
      elif 'who are you' in query:
          speak("I am your virtual voice assistant to help you sir\n")   

      elif 'shutdown' in query:
           speak("Wait a secound sir, the systen is being shutdown\n")
           subprocess.call('shutdown / p /f')   

      elif 'exit' in query:
           speak("Thak you sir  for choosing me as your voice assistant\n")     
           exit()

      elif 'friend' in query:
           speak("Yes,I will be your friend\n")
           
