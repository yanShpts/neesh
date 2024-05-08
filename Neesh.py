import tkinter as tk
from tkinter import *
from tkinter import ttk
from pytrends.request import TrendReq

past_entries = []  # List of tuples to store past results

class Neesh:

    def __init__(self, root):
        # Initialize the main window
        root.title("Neesh")
        root.configure(bg='light grey')
        root.minsize(800, 600)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Create the main frame
        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=0)

        # Create variables to store user input and display output
        self.interest = tk.StringVar()
        self.display = tk.StringVar()
        self.display.set('Find your score!')

        # Create the Leaderboard section
        leader_Title = ttk.Label(mainframe, text="Leaderboard", font=("Verdana 16 underline")).grid(column=0, row=4, sticky=(W, E))
        self.leaderboard = tk.StringVar()  # Variable to store the leaderboard data

        # Create the Recent Entries section
        last_5_Title = ttk.Label(mainframe, text="Recent Entries", font=("Verdana 16 underline")).grid(column=1, row=4, sticky=(W, E))
        self.lastEntries = tk.StringVar()  # Variable to store the recent entries data

        # Create the main label
        label = ttk.Label(mainframe, text="Neesh", font=("Verdana bold", 24), anchor="center")
        label.grid(column=0, row=0, sticky=(W, E))

        # Create the input entry field
        self.interestEntry = ttk.Entry(mainframe, textvariable=self.interest)
        self.interestEntry.grid(column=0, row=1, sticky=(W, E))
        # Bind the 'Return' key to the 'neeshify' function
        self.interestEntry.bind('<Return>', self.neeshify)

        # Create the "Send" button
        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=1, row=1, sticky=(W, E))
        # Create labels to display output
        ttk.Label(mainframe, textvariable=self.display, font=("Verdana 15"), anchor="center").grid(column=0, row=3, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.leaderboard, font=("Verdana 12")).grid(column=0, row=5, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.lastEntries, font=("Verdana 12")).grid(column=1, row=5, sticky=(W, E))

    def neeshify(self, event=None):
        # Get the interest data and calculate the niche score
        nicheList = self.getInterest(self.interest)
        self.getNiche(nicheList)
        self.interestEntry.delete(0, 'end')  # Clear the text box

    def getInterest(self, interest):
        # Initialize the TrendReq object
        pytrends = TrendReq(hl='en-US', tz=360)
        interest = str(self.interest.get())
        kw_list = ['food near me', interest]  # The keyword(s) to get results for
        # Build the payload for the Google Trends API request
        pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
        # Get the interest data over the last month
        trends = pytrends.interest_over_time()

        return trends[interest].tolist()  # Return the interest data as a list

    def getNiche(self, nicheList):
        interest = str(self.interest.get())
        # Calculate the niche score based on the interest data
        neesh = int(1000 - (10 * sum(nicheList) / len(nicheList)))
        if (interest, neesh) not in past_entries:
            past_entries.append((interest, neesh))  # Add new entry to the past entries list
        self.display.set(interest + " has a neesh score of: " + str(neesh))  # Display the niche score
        self.updateLeaderboard()  # Update the leaderboard
        self.updateLastEntries()  # Update the recent entries

    def updateLeaderboard(self):
        # Sort the past entries by niche score in descending order
        sortedEntries = sorted(past_entries, key=lambda x: x[1], reverse=True)
        topEntries = sortedEntries[:5]  # Get the top 5 entries
        # Create a string to display the leaderboard
        leaderboardString = "\n".join(f"{entry[0]}: {entry[1]}" for entry in topEntries)
        self.leaderboard.set(leaderboardString)  # Update the leaderboard display

    def updateLastEntries(self):
        lastEntries = past_entries[-5:]  # Get the last 5 entries
        # Create a string to display the recent entries
        lastEntriesString = "\n".join(f"{entry[0]}: {entry[1]}" for entry in reversed(lastEntries))
        self.lastEntries.set(lastEntriesString)  # Update the recent entries display

# Create the main window and run the application
root = tk.Tk()
Neesh(root)
root.mainloop()