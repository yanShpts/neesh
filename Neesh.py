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

       
# create a root Tk object
root = tk.Tk()

# create a FeetToMeters object with the Tk root object as an argument
Neesh(root)

# call the mainloop method on the Tk root object
root.mainloop()