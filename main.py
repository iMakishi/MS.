# Imports

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import random
import json

# Global Variables

xFolder = ""
movieResult = ""

# MAIN Definitions

def close(x):
    x.destroy()

def storeFolder(x):
    filename = "folderPath.json"
    try:
        with open(filename, "w") as filePath:
            json.dump(x, filePath)
        print("Folder stored ----> SUCCESSFULL!")
    except:
        print("Folder stored ----> UNSUCCESSFULL!")

# GUI Definitions

def selectFolder(self): # Opens Windows file explorer and stores the file selected in a global variable.
    global xFolder
    xFolder = filedialog.askdirectory(title = "Select Folder")
    storeFolder(xFolder)

def customizeAppearance(self):
    print("Appearance")

def customizeSettings(self):
    print("Settings")

def releaseNotes(self):
    releaseNotesWindow = Toplevel()

    "------------------------------------------------------"

    # Window bar
    releaseNotesWindow.title("Release Notes")
    #releaseNotesWindow.resizable(0, 0)

    # Window size and position
    w = 450 # Width for the Tk window.
    h = 550 # Height for the Tk window.

    ws = releaseNotesWindow.winfo_screenwidth() # Width of the screen.
    hs = releaseNotesWindow.winfo_screenheight() # Height of the screen.

    # X and Y coordinates for the Tk window.
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Dimensions of the screen and where it is placed.
    releaseNotesWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Window background color
    releaseNotesWindow.configure(bg = "black")

    " Top Frame -------------------------------------------"

    topFrame = Frame(releaseNotesWindow, bg = "white")
    topFrame.pack()

    # Window title ------------------------------ #
    windowTitleLabel = Label(topFrame, text = "Release Notes",
        bg = "white",
        font = ("Courier New", 15, "underline")
    )
    windowTitleLabel.pack(
        pady = (10,5)
    )

    " Middle Frame ----------------------------------------"

    middleFrame = Frame(releaseNotesWindow, bg = "green")
    middleFrame.pack(fill = BOTH)

    # Text 
    

    # Right side text Scrollbar



    " Bottom Frame ----------------------------------------"

    bottomFrame = Frame(releaseNotesWindow, bg = "white")
    bottomFrame.pack()

    # Close release notes window --------------- #
    closeButton = Button(bottomFrame, text = "Close",
        bg = "white",
        relief = SOLID,
        font = ("Courier New", 12),
        command = lambda: close(releaseNotesWindow)
    )
    closeButton.pack(
        side = TOP,
        pady = (10, 10),
        ipadx = 61,
        ipady = 5
    )

    # License label ---------------------------------- #
    licenseLabel = Label(bottomFrame, text = "@2021 by Maximiliano E. Lutz",
        bg = "white",
        font = ("Courier New", 10, "underline")
    )
    licenseLabel.pack(
        side = BOTTOM,
        pady = 5,
        ipady = 5
    )

    "------------------------------------------------------"

    releaseNotesWindow.mainloop()

def reportProblem(self):
    print("Report a problem")

def appAbout(self):
    print("About")

def randomChoice(self):
    try:
        filename = "folderPath.json"
        with open(filename) as filePath:
            movieFolder = os.listdir(json.load(filePath))
            for x in range(1):
                movieResult = random.choice(movieFolder)
                self.displayResultLabel.config(text = movieResult)
    except FileNotFoundError:
        try:
            movieFolder = os.listdir(xFolder)
            for x in range(1):
                movieResult = random.choice(movieFolder)
                self.displayResultLabel.config(text = movieResult)
        except FileNotFoundError:
            selectFolder(self)

def playChoice(self):
    print("Play selected movie")

