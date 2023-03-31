import tkinter
import tkinter.ttk
import tkinter.messagebox
from Database import *
from DatabaseView import *

class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "Please enter client ID to " + task

        # Labels
        tkinter.Label(window, text = self.heading, width = 50).grid(pady = 20, row = 1)
        tkinter.Label(window, text = "client ID", width = 10).grid(pady = 5, row = 2)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width = 5, textvariable = self.id)

        self.idEntry.grid(pady = 5, row = 3)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width = 20, text = task, command = self.Search).grid(pady = 15, padx = 5, column = 1, row = 14)
        elif (task == "Delete"):
            tkinter.Button(window, width = 20, text = task, command = self.Delete).grid(pady = 15, padx = 5, column = 1, row = 14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)
    
    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())