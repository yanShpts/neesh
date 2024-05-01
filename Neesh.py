import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd 
from pytrends.request import TrendReq

past_entries = [] #list of tuples to store past results

class Neesh:

    def __init__(self, root):

        root.title("Neesh")
        root.configure(bg='light grey')
        root.minsize(800,600)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=0)

        self.interest = tk.StringVar()

        self.display = tk.StringVar()
        self.display.set('Find your score!')

        #LEADERBOARD
        leader_Title = ttk.Label(mainframe, text="Leaderboard", font=("Verdana 16 underline")).grid(column=0, row=4, sticky=(W,E)) # separate title label to allow for separate styling
        self.leaderboard = tk.StringVar()   # the actual leaderboard list
        
        #LAST 5 ENTRIES
        last_5_Title = ttk.Label(mainframe, text="Recent Entries", font=("Verdana 16 underline")).grid(column=1, row=4, sticky=(W,E))  # separate title label to allow for separate styling
        self.lastEntries = tk.StringVar()   # the actual past entries list

        label = ttk.Label(mainframe, text="Neesh", font=("Verdana bold", 24), anchor="center")

        label.grid(column=0, row=0, sticky=(W,E))

        self.interestEntry = ttk.Entry(mainframe, textvariable=self.interest)
        self.interestEntry.grid(column=0, row=1, sticky=(W,E))
        #bind return/enter 
        self.interestEntry.bind('<Return>', self.neeshify)

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=1, row=1, sticky=(W,E))
        ttk.Label(mainframe, textvariable=self.display, font=("Verdana 15"), anchor="center").grid(column=0, row=3, sticky=(W,E))
        ttk.Label(mainframe, textvariable=self.leaderboard, font=("Verdana 12")).grid(column=0, row=5, sticky=(W,E))
        ttk.Label(mainframe, textvariable=self.lastEntries, font=("Verdana 12")).grid(column=1, row=5, sticky=(W,E)) 


    def neeshify(self, event=None):
            nicheList = self.getInterest(self.interest)
            self.getNiche(nicheList)
            self.interestEntry.delete(0, 'end')  # Clear the text box

    def getInterest(self, interest):
        pytrends = TrendReq(hl='en-US', tz=360) 
        interest = str(self.interest.get())
        kw_list = ['food near me',interest] #the keyword to get results for 
        pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='') #builds payload for keyword and interest over last 12 months
        trends = pytrends.interest_over_time()

        return trends[interest].tolist()
    
    def getNiche(self, nicheList):
        interest = str(self.interest.get())
        neesh = int(1000-(10*sum(nicheList)/len(nicheList)))
        if (interest, neesh) not in past_entries:
            past_entries.append((interest, neesh))
        self.display.set(interest + " has a neesh score of: " + str(neesh))
        self.updateLeaderboard()
        self.updateLastEntries()

    def updateLeaderboard(self):
        sortedEntries = sorted(past_entries, key=lambda x: x[1], reverse=True)
        topEntries = sortedEntries[:5]
        leaderboardString = "\n".join(f"{entry[0]}: {entry[1]}" for entry in topEntries)
        self.leaderboard.set(leaderboardString)

    def updateLastEntries(self):
        lastEntries = past_entries[-5:]
        lastEntriesString = "\n".join(f"{entry[0]}: {entry[1]}" for entry in reversed(lastEntries))
        self.lastEntries.set(lastEntriesString)

root = tk.Tk()
Neesh(root)
root.mainloop()