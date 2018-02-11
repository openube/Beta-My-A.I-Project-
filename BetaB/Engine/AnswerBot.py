
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


import requests

class AnswerBot:
    def __init__(self,url):
        self.driver=webdriver.PhantomJS()
        self.driver.wait=WebDriverWait(self.driver,5)
        self.url=url
        self.ansbot()
        self.person_ans()
        
    def ansbot(self):
        self.driver.get(self.url)

        soup=BeautifulSoup(self.driver.page_source,"html.parser")
        answer=soup.find_all(class_="_sPg")
        if answer:
            answer=(answer[0].get_text())
            if (answer[:4])=='http' or (answer[:3])== "www":
                    answer=[]
                
        if not answer:            
            links=soup.find_all("div",{'class':"s"})
            items=[]
        
            for item in links:
                item=(item.find("span",{'class':"st"}))
                items.append(item.get_text())
        
            answer=(items[1])
        
#         with open("twst.html","w+") as f:
#             f.write(str(soup))
        if not answer:
            answer=soup.find_all(class_="_m3b")
            if answer:
                answer=(answer[0].get_text())
                if (answer[:4])=='http' or (answer[:3])== "www":
                    answer=[]
        if not answer:
            answer=soup.find_all(class_="kv")
            if answer:
                answer=(answer[0].get_text())
                if (answer[:4])=='http' or (answer[:3])== "www":
                    answer=[]

            
        
        if not answer:
            answer=soup.find_all(id="_vBb")
            if answer:
                items=(answer[0].text)
                if (answer[:4])=='http' or (answer[:3])== "www":
                    answer=[]
                else:
                    answer=items.split(",")
                    answer=answer
                    
    
                     
        return answer
    
    def person_ans(self):
        r=requests.get(self.url)
        soup=BeautifulSoup(r.text,"html.parser")
        links=soup.find_all("div",{'class':"s"})
        items=[]
        
        for item in links:
            item=(item.find("span",{'class':"st"}))
            items.append(item.get_text())

        answer=(items[1])
        print(answer)
        return answer

                
        
    
        
        