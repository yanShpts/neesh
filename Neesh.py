import tkinter as tk
from tkinter import ttk
import pandas as pd 
from pytrends.request import TrendReq

class Neesh:

    def __init__(self, root):

        root.title("Neesh")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)

        self.interest = tk.StringVar()
        self.score = 'Find your score!'

        interestEntry = ttk.Entry(mainframe, textvariable=self.interest, justify="left")
        interestEntry.grid(column=1, row=1, rowspan=3)

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=2, row=3)
        ttk.Label(mainframe, textvariable=self.score).grid(column=3, row=4)

    def neeshify(self):
            pytrends = TrendReq(hl='en-US', tz=360)
            try:
                nicheList = self.getInterest(self.interest)
                self.getNiche(nicheList)
            
            except:
                print("Error! Try again.")

    def getInterest(self, interest):
        pytrends = TrendReq(hl='en-US', tz=360) 
        interest = str(self.interest.get())
        kw_list = ['food near me',interest] #the keyword to get results for 
        pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='') #builds payload for keyword and interest over last 12 months
        trends = pytrends.interest_over_time()

        return trends[interest].tolist()
    
    def getNiche(self, nicheList):
        self.score = 100-(sum(nicheList)/len(nicheList))
        print(self.score)
                

       
root = tk.Tk()
Neesh(root)
root.mainloop()