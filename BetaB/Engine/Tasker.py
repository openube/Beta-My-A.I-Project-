'''
Created on Feb 7, 2018

@author: DJETHA
'''
import requests
import simplejson as json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import pyttsx3
import csv
from urllib.request import urlopen
import speech_recognition as sr

class Fetcher:
    #This can be used for any google search but it is restricted to searching for places and their descriptions
    def lookup(self,text):
        
        params={"q":text}
        r=requests.get("http://www.bing.com/search",params=params)
        
        soup=BeautifulSoup(r.text,"html.parser")
        
        # for bing items and sub items fall under this category
        results=soup.find("ol",{"id":"b_results"})
        links=results.find_all("li",{"class":"b_algo"})
        file=open("./Searchitem.txt","w+")
        for item in links:
            Item_text=item.find("a").text 
            
            item_href=item.find("a").attrs["href"]
            
            file.write("Name: "+Item_text+"\n")
            file.write("Summary: "+(item.find("a").parent.parent.find("p").text)+"\n")
        file.close()
        file=open("./Searchitem.txt","r+")
        file=file.read()
        engine=pyttsx3.init() 
        engine.say(file);
        engine.runAndWait() ;
        Fetcher().OpenUrl( text)
        
    #This is the extension of the look command
    #This lets you make choices from the options specified in the lookup
    #Then if the link exists it opens in your browser
    def OpenUrl(self,text):
        r=sr.Recognizer()
        jsonfile=open("./BetaB/json/MyJson.json","r+") 
        google=jsonfile.read()
        params={"q":text}
        urllink=requests.get("http://www.bing.com/search",params=params)
        
        soup=BeautifulSoup(urllink.text,"html.parser")
        old_file=open("./ages.json","w")
        # for bing items and sub items fall under this category
        results=soup.find("ol",{"id":"b_results"})
        links=results.find_all("li",{"class":"b_algo"})
        data={}
        with open("./info.json","w") as file:
            for item in links:
                Item_text=item.find("a").text 
                item_href=item.find("a").attrs["href"]
                
                data[Item_text]=item_href
            
            file.write(json.dumps(data))
        file=open("./info.json","r+")
        file=file.read()
        data=json.loads(file)
        engine=pyttsx3.init()
        import webbrowser
        link=""
        with sr.Microphone() as source:
            engine.say("which would you like open? ")
            engine.runAndWait()
            choice=r.listen(source)
            choice=r.recognize_google_cloud(choice, credentials_json=google)
            choice=choice.title()
            choice=choice.split("'",1)[0]
        for item in data:
            if item.__contains__(choice):
                link= data[item]
                break
        webbrowser.open(link)

          
    def News(self):
        News_url=urlopen("http://www.bing.com/news?")
        soup=BeautifulSoup(News_url,"lxml")
        titles=soup.find_all("div",{"class":"caption"})
        file=open("./News.txt","w+")
        for title in titles:
            if title.strong is not  None:
                Header=title.strong.text
                file.write(Header+"\n")
            else:
                header=title.find("a",{"class","title"})
                Header=header.contents[0]
                file.write(Header+"\n")
        file.close()
        file=open("./News.txt","r+")
        file=file.read()
        engine=pyttsx3.init() 
        engine.say(file);
        engine.runAndWait() ; 
        
    def Nearbyplaces(self,text):
        r=requests.get("https://www.google.ca/search?q="+text)
        soup=BeautifulSoup(r.text,"html.parser")
        answer=soup.find("div",{'class': ['_Arj',"g"]})
        divs=answer.find_all("div")
        engine=pyttsx3.init()
        for div in divs:
            tds=(div.find_all("td"))
            if tds:
            
                divs=(div.find_all("div"))
                div=' '
                title=(divs[0].get_text())
                if not text.__contains__(title.lower()):
                    div=(divs[0].get_text())
                div1=(divs[1].get_text())
                num=div1.find("(")
        
                if not num==-1: 
                    div1=(div1[:num-2])
                try:
                    if isinstance(float(div1), float):
                        div1=''
                except:
                    div1=div1
                div2=(divs[2].get_text())
                num1=div2.find("(")
               
                if not num1==-1:
                    div2=(div2[:num1-2])
                div3=(divs[3].get_text())
                div5=''
                if len(divs) >3 and not div1:
                    div5=(divs[5].get_text())
                    num2=div5.find("(")
        
                    if not num2==-1:
                        div5=(div5[:num2-2])
                print(div1, div5)
             
                engine.say(div)
                engine.runAndWait() ;
                engine.say(div1)
                engine.runAndWait() ;
                engine.say(div2)
                engine.runAndWait() ;
                engine.say(div3)
                engine.runAndWait() ;
                engine.say(div5)
                engine.runAndWait() ;
                        
                            
                        
