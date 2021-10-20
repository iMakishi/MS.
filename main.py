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
    #releaseNotesWindow.overrideredirect(True)
    releaseNotesWindow.title("About")
    releaseNotesWindow.resizable(0, 0)

    # Window size and position
    w = 400 # Width for the Tk window.
    h = 525 # Height for the Tk window.

    ws = releaseNotesWindow.winfo_screenwidth() # Width of the screen.
    hs = releaseNotesWindow.winfo_screenheight() # Height of the screen.

    # X and Y coordinates for the Tk window.
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Dimensions of the screen and where it is placed.
    releaseNotesWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Window background color
    releaseNotesWindow.configure(bg = "white")

    " Top Frame -------------------------------------------"

    topFrame = Frame(releaseNotesWindow, bg = "white")
    topFrame.pack()


    releaseNotesTitleLabel = Label(topFrame, text = "Release Notes",
        bg = "white",
        font = ("Courier New", 30, "underline")
    )
    releaseNotesTitleLabel.pack(
        pady = 5
    )

    " Middle Frame ----------------------------------------"

    middleFrame = Frame(releaseNotesWindow, bg = "white")
    middleFrame.pack()

    releaseNotesText = Text(middleFrame,
        relief = FLAT)
    releaseNotesText.configure(state = "disabled")
    releaseNotesText.pack(
        side = LEFT,
        padx = 10,
        pady = 10
    )

    textScrollbar = Scrollbar(middleFrame, orient = VERTICAL,
        command = releaseNotesText.yview()
    )
    textScrollbar.pack(
        side = RIGHT
    )

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
        side = BOTTOM,
        pady = (10, 10),
        ipadx = 61,
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

