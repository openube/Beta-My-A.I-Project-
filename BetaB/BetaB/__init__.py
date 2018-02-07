'''
Created on Feb 6, 2018

@author: DJETHA
This covers the frontal core of the A.I program. It is from this point you initiate the program, providing 
all the required information search for what you need
'''
from MainEngine import MainEngine
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3;
from time import sleep
#The running is used to help end the program loop once the required information has been gotten
running=True
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
    #The speech recognizer microphone is renamed as source     
    with sr.Microphone() as source:
        r=sr.Recognizer()
        engine=pyttsx3.init() 
        #The microphone is caliberated with the ambient sound to aid clarity
        engine.say("Please wait. Calibrating microphone...")  
        r.adjust_for_ambient_noise(source, duration=5)  
        engine=pyttsx3.init()   
        engine.say("My name is Bytes B version 1.0 . What is your name?")
        engine.runAndWait() ;
        play_audio("start.wav")
        name=r.listen(source)
        name=r.recognize_google(name)
        engine.say("Nice to meet you "+ name)
        engine.say("Thats good to hear")
        engine.say("What would you like to do today")
        engine.runAndWait() ;
        play_audio("start.wav")
        print("Begin speaking...")
        audio=r.listen(source)
        
    global running
    command=''
    try:
        command=r.recognize_google(audio)
        play_audio("start.wav")
        print("Your command is: "+ command)
        running=False
    
    except:
        initSpeech()

    if command in ["exit","quit","end","googbye"]:
        running=False
    cmd.discover(command)
  
 

while running==True:
    initSpeech()