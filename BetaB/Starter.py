'''
Created on Feb 6, 2018

@author: udendu abasili
This covers the frontal core of the A.I program. It is from this point you initiate the program, providing 
all the required information search for what you need
'''
import simplejson as json
from BetaB.Engine.MainEngine import MainEngine
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3;
from time import sleep
import sys
#The running is used to help end the program loop once the required information has been gotten
running=''
cmd=MainEngine()


#This is of no concern to user as it just helps play the wav file
def play_audio(filename):

    chunk=1024
   
    wf=wave.open(filename,"rb")

    pa=pyaudio.PyAudio()

    stream=pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
        )
    

    data_stream=wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream=wf.readframes(chunk)
    stream.close()
    pa.terminate()


def initSpeech():
    jsonfile=open("./BetaB/json/MyJson.json","r+") 
    
    data=jsonfile.read()
    
    global running
    #The speech recognizer microphone is renamed as source     
    with sr.Microphone() as source:
        r=sr.Recognizer()
        r.energy_threshold=1000
        r.phrase_threshold=0
        engine=pyttsx3.init() 
        
        #The microphone is caliberated with the ambient sound to aid clarity
        engine.say("Please wait. Calibrating microphone...")
        engine.runAndWait() ;  
        engine.say("My name is Beta B version 1.0 . What is your name?")
        engine.runAndWait() ;
        name=r.listen(source)
        print(name)
        name=r.recognize_google_cloud(name, credentials_json=data)
        play_audio("./BetaB/audio/start.wav")
        engine.say("Nice to meet you "+ name)
        engine.runAndWait() ;
        engine.say("What would you like to do today")
        engine.runAndWait() ;
        print("Begin speaking...")
        print(running)
        task=r.listen(source) 
    try:
        
        command=r.recognize_google_cloud(task, credentials_json=data)
        
        running=False

    except:
        engine.say("sorry didnt get that. Please try again")
        engine.runAndWait() ;
        running=True
        
    if command in ["exit","quit","end","googbye"]:
        engine.say("Shutting Down")
        engine.runAndWait() ;
        running=False
    cmd.discover(command)
    
  
 
print(running)
while running==True:
    initSpeech()