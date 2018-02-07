'''
Created on Feb 6, 2018

@author: udendu abasili
This is the main engine that holds most of the commands that the A.I would deal with. It is at this point
that the text said by user would be filtered to match the specifications of the user
'''
from weather import Weather
import speech_recognition as sr
import urllib
import re
import webbrowser
import subprocess
import os
import pyttsx3;
from os.path import join
from .Tasker import Fetcher


class MainEngine:
    engine=pyttsx3.init()
    global weather
    weather = Weather()
    def __init__(self):
        self.confirm=["yes","affirmative","si","sure","postivie","yeah","do it","confirm"]
        self.cancel=["no","negative","negative soldier","wait","cancel","nope","dont  it","deny"]
        
    def discover(self,text):
        jsonfile=open("./BetaB/json/MyJson.json","r+") 
        data=jsonfile.read()
        if "weather" in text:
            with sr.Microphone() as source:
                r=sr.Recognizer()
                engine=pyttsx3.init()   
                engine.say("Where would like to look?")
                engine.runAndWait() ;
                print("Listening...")
                audio=r.listen(source)
            loc=r.recognize_google_cloud(audio, credentials_json=data)
            lookup = weather.lookup(560743)
            condition = lookup.condition()
            print(condition.text())
            
            # Lookup via location name.
            file=open("./weather.txt","w+")
            location = weather.lookup_by_location(loc)
            condition = location.condition()
            print(condition.text())
            
            # Get weather forecasts for the upcoming days.
            
            forecasts = location.forecast()
            for forecast in forecasts:
                file.write("Date:"+forecast.date()+"\n")
                file.write("Weather:"+forecast.text()+"\n")
                file.write("High Temperature:"+forecast.high()+"degrees"+"\n")
                file.write("Low Temperature:"+forecast.low()+"degrees"+"\n")
            file.close()
            file=open("./weather.txt","r+")
            file=file.read()
            engine.say(file);
            engine.runAndWait() ; 

            
        elif "play" in text:
            if "music" in text:
                with sr.Microphone() as source:
                    r=sr.Recognizer()
                    engine=pyttsx3.init()   
                    engine.say("Cool! Which artist?")
                    engine.runAndWait() ;
                    audio=r.listen(source)
                artist=r.recognize_google_cloud(audio, credentials_json=data)
                query_string = urllib.parse.urlencode({"search_query" : artist})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                web=("http://www.youtube.com/watch?v=" + search_results[0])
                webbrowser.open(web)
            else:
                artist= text.split(" ",1)[-1]
                print(artist)
                query_string = urllib.parse.urlencode({"search_query" : artist})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                web=("http://www.youtube.com/watch?v=" + search_results[0])
                webbrowser.open(web)
            
        elif "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You havent told me your name")
            else:
                self.respond("My name is python command. How are you?")
        elif "launch" in text:
            app =text.split(" ", 1)[-1]
            app=app.lower()
            app=(app+".exe")
            loc1=os.walk("C:\Program Files")
            loc2=os.walk('C:\Program Files (x86)')

            for root, dirs, files in loc2:
                if files.__contains__(app):
                    root=root
            
                    root=join(root, app)
                    print(root)
                    break
                    exit()
            else:
                for root, dirs, files in loc1:
                    print ("searching", root)
                    if root.__contains__(app):
                        print ("found: %s" % join(root, app))
                        break
            subprocess.call(root)
        elif "lookup" in text:
            text=text.split(" ",1)[-1]
            f=Fetcher().lookup(text)
        elif "look up" in text:
            text=text.split(" ",2)[-1]
            f=Fetcher().lookup(text)
        elif "news" in text:
            news=Fetcher().News()
        
            
            
    def respond(self,response):
        engine=pyttsx3.init()
        engine.say(response)
        engine.runAndWait() ;  
        
        