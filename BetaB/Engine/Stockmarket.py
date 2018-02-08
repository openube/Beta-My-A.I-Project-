'''
Created on Jan 18, 2018

@author: DJETHA
'''
'''
Created on Jan 18, 2018

@author: udendu abasili
'''
from urllib.request import urlopen
import requests
import csv
from bs4 import BeautifulSoup
import pyttsx3
#This reads out the companies and their stock price changes in the market


def Stock_market() :
    params="stock market"
    params={"q":params}
    r=requests.get("http://www.bing.com/search",params=params)
    soup=BeautifulSoup(r.text,"html.parser")
    file=csv.writer(open("Stocks.csv","w"))
    
    items=soup.find("ol",{"id":"b_results"})
    lists=items.find_all("li",{"class":"b_algo"})
    for item in lists:
        names=item.find("a").text
        links=item.find("a").attrs["href"]
        if names and links:
            link=(links)
        break
    
    link=urlopen(link)
    soup=BeautifulSoup(link,"html.parser")
    
    items=soup.find_all("li",{"class":"row"})
    
    #This is an easy way of extracting data
    #Basically we look the tag that has a collection under a single
    #
    for item in items:
        code=item.find_all("span")
    
        if (len(code))>2:
            
            Name = str(code[0].get_text())
            if not Name.__contains__("yield"):
                Company=Name
            StockPrice=str((code[1]).get_text())
            if  StockPrice[0].isnumeric() and StockPrice[-1].isnumeric():
                StockPrice=StockPrice
            if  StockPrice[0].isnumeric() and StockPrice[-1].isnumeric():
                StockPrice=("$"+StockPrice)
            if not StockPrice[-1].isnumeric():
                StockPrice=" "
            Stock=str(code[2].get_text())
            if Stock.__contains__("%"):
                Stock_perc=Stock
                
    
            stocks=file.writerow([Company,StockPrice,Stock_perc])
    file=open("Stocks.csv","r")
    engine=pyttsx3.init()
    engine.say("The following are Companies and their stock price changes: ")
    engine.say("Stock Prices would be given if available ")
    engine.say(file.read())
    engine.runAndWait()
    
