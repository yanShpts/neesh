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

        interestEntry = ttk.Entry(mainframe, textvariable=self.interest, justify="left")
        interestEntry.grid(column=1, row=1, rowspan=2)

        ttk.Button(mainframe, text="Send", command=self.neeshify).grid(column=3, row=3)

    def neeshify(self):
            pytrends = TrendReq(hl='en-US', tz=360)
            try:
                interest = str(self.interest.get())
                kw_list = [interest] #the keyword to get results for 
                pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='') #builds payload for keyword and interest over last 12 months
                print(pytrends.interest_over_time())
            except:
                print("Error! Try again.")

                

       
root = tk.Tk()
Neesh(root)
root.mainloop()