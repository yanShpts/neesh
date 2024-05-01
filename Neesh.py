import tkinter as tk
from tkinter import ttk
import pandas as pd 
from pytrends.request import TrendReq

past_entries = [] #list of tuples to store past results

class Neesh:

    def __init__(self, root):

        root.title("Neesh")
        root.configure(bg='light grey')

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.interest = tk.StringVar()
        self.score = tk.StringVar()
        self.score.set('Find your score!')

        ttk.Label(mainframe, text="Neesh", font=("Arial", 24)).grid(column=1, row=0, sticky=tk.W)

        interestEntry = ttk.Entry(mainframe, textvariable=self.interest, justify="center")
        interestEntry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=1, row=2, sticky=tk.W)
        ttk.Label(mainframe, textvariable=self.score).grid(column=1, row=3, sticky=(tk.W, tk.E))

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
        interest = str(self.interest.get())
        self.score = 100-(sum(nicheList)/len(nicheList))
        past_entries.append((interest, self.score))
        print(past_entries)
                

       
root = tk.Tk()
Neesh(root)
root.mainloop()