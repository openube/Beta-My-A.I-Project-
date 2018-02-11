from BetaB.Starter import initSpeech

from PIL import Image, ImageTk

from tkinter.ttk import Frame, Button, Label, Style
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.constants import  LEFT

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        
        self.pack(fill=BOTH, expand=True)
        
        
        Quitbutton = Button(self, text="QUIT",command=quit)
        Quitbutton.pack(side=RIGHT)
        okButton = Button(self,text="ACTIVATE",command= self.BetaB)
        okButton.pack(side=LEFT)
        
        self.master.title("BETA B V1.0")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#000000")
        
        bard = Image.open("VA.png")
        bard = bard.resize((300, 260))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)
        label1.size()
        
     
        



    def BetaB(self):
        file=initSpeech()  
        
               

def main():
  
    root = Tk()
    root.geometry("300x300+300+300")
    root.iconbitmap('ai_6mX_icon.ico')
    app = Example()
    root.mainloop()  
    

if __name__ == '__main__':
    main()  

