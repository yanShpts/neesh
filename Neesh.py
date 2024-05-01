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
        self.leaderboard = tk.StringVar()
        self.leaderboard.set('Leaderboard:')

        ttk.Label(mainframe, text="Neesh", font=("Arial", 24)).grid(column=1, row=0, sticky=tk.W)

        self.interestEntry = ttk.Entry(mainframe, textvariable=self.interest, justify="center")
        self.interestEntry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=1, row=2, sticky=tk.W)
        ttk.Label(mainframe, textvariable=self.score).grid(column=1, row=3, sticky=(tk.W, tk.E))
        ttk.Label(mainframe, textvariable=self.leaderboard).grid(column=1, row=4, sticky=(tk.W, tk.E))

    def neeshify(self):
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
        self.update_leaderboard()

        return trends[interest].tolist()
    
    def getNiche(self, nicheList):
        interest = str(self.interest.get())
        neesh = int(1000-(10*sum(nicheList)/len(nicheList)))
        self.score.set(neesh)  # Update the score
        if (interest, self.score) not in past_entries:
            past_entries.append((interest, neesh))
        self.score.set("Your neesh score is: " + str(neesh))
        print(past_entries)

    def update_leaderboard(self):
        # Sort the past_entries list by score in descending order
        sorted_entries = sorted(past_entries, key=lambda x: x[1], reverse=True)
        # Take the top 5 entries
        top_entries = sorted_entries[:5]
        # Format the leaderboard string
        leaderboard_str = "Leaderboard:\n" + "\n".join(f"{entry[0]}: {entry[1]}" for entry in top_entries)
        # Update the leaderboard label
        self.leaderboard.set(leaderboard_str)
                
    
                

       
root = tk.Tk()
Neesh(root)
root.mainloop()