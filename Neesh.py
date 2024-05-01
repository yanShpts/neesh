import tkinter as tk
from tkinter import ttk
import pandas as pd 
from pytrends.request import TrendReq

pastEntries = [] #list of tuples to store past results

class Neesh:

    def __init__(self, root):

        root.title("Neesh")
        root.configure(bg='light grey')

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.interest = tk.StringVar()

        self.display = tk.StringVar()
        self.display.set('Find your score!')

        self.leaderboard = tk.StringVar()
        self.leaderboard.set('Leaderboard:')

        self.lastEntries = tk.StringVar() # New variable to store the last 5 entries
        self.lastEntries.set('Last 5 Entries:')

        ttk.Label(mainframe, text="Neesh", font=("Arial", 24)).grid(column=1, row=0, sticky=tk.W)

        self.interestEntry = ttk.Entry(mainframe, textvariable=self.interest, justify="center")
        self.interestEntry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=1, row=2, sticky=tk.W)
        ttk.Label(mainframe, textvariable=self.display).grid(column=1, row=3, sticky=(tk.W, tk.E))
        ttk.Label(mainframe, textvariable=self.leaderboard).grid(column=1, row=4, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, textvariable=self.lastEntries).grid(column=2, row=4, sticky=(tk.W, tk.E)) # New label to display the last 5 entries



    def neeshify(self, event=None):
            pytrends = TrendReq(hl='en-US', tz=360)
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
        if (interest, neesh) not in pastEntries:
            pastEntries.append((interest, neesh))
        self.display.set(interest + " has an neesh score of: " + str(neesh))
        self.updateLeaderboard()
        self.updateLastEntries()

    def updateLeaderboard(self):
        sortedEntries = sorted(pastEntries, key=lambda x: x[1], reverse=True)
        topEntries = sortedEntries[:5]
        leaderboardString = "Leaderboard:\n" + "\n".join(f"{entry[0]}: {entry[1]}" for entry in topEntries)
        self.leaderboard.set(leaderboardString)

    def updateLastEntries(self):
        lastEntries = pastEntries[-5:]
        lastEntriesString = "Last 5 Entries:\n" + "\n".join(f"{entry[0]}: {entry[1]}" for entry in reversed(lastEntries))
        self.lastEntries.set(lastEntriesString)

root = tk.Tk()
Neesh(root)
root.mainloop()