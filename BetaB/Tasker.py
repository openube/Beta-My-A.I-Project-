'''
Created on Feb 7, 2018

@author: DJETHA
'''
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import pyttsx3
import csv
from urllib.request import urlopen


class Fetcher:
    #This can be used for any google search but it is restricted to searching for places and their descriptions
    def lookup(self,text):
        params={"q":text}
        r=requests.get("http://www.bing.com/search",params=params)
        
        soup=BeautifulSoup(r.text,"html.parser")
        
        # for bing items and sub items fall under this category
        results=soup.find("ol",{"id":"b_results"})
        links=results.find_all("li",{"class":"b_algo"})
        file=open("Searchitem.txt","w+")
        for item in links:
            Item_text=item.find("a").text 
            
            item_href=item.find("a").attrs["href"]
            
            file.write("Name: "+Item_text+"\n")
            file.write("Summary: "+(item.find("a").parent.parent.find("p").text)+"\n")
        file.close()
        file=open("Searchitem.txt","r+")
        file=file.read()
        engine=pyttsx3.init() 
        engine.say(file);
        engine.runAndWait() ; 
    #This is gives you the headlines for the daily news   
    def News(self):
        News_url=urlopen("http://www.bing.com/news?")
        soup=BeautifulSoup(News_url,"lxml")
        titles=soup.find_all("div",{"class":"caption"})
        file=open("News.txt","w+")
        for title in titles:
            if title.strong is not  None:
                Header=title.strong.text
                file.write(Header+"\n")
            else:
                header=title.find("a",{"class","title"})
                Header=header.contents[0]
                file.write(Header+"\n")
        file.close()
        file=open("News.txt","r+")
        file=file.read()
        engine=pyttsx3.init() 
        engine.say(file);
        engine.runAndWait() ; 
                
                        
                        
