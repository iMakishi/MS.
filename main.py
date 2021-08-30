# Imports

import tkinter
from tkinter import *
from tkinter import filedialog
import os
import random

# Global Variables

xFolder = ""
movieResult = ""

# MAIN Definitions

def close(x):
    x.destroy()

# GUI Definitions

def selectFolder(self): # Opens Windows file explorer and stores the file selected in a global variable.
    global xFolder
    xFolder = filedialog.askdirectory(title = "Select Folder")

def customizeAppearance(self):
    print("Appearance")

def customizeSettings(self):
    print("Settings")

def releaseNotes(self):
    print("Release Notes")
    # new top window without upper bar
    # label with release notes
    # scrollbar if release notes are an extensive .txt
    # close button

def reportProblem(self):
    print("Report a problem")

def aboutApplication(self):
    aboutWindow = Toplevel()

    "------------------------------------------------------"

    # Window bar
    #aboutWindow.overrideredirect(True)
    aboutWindow.title("About")
    aboutWindow.resizable(0, 0)

    # Window size and position
    w = 400 # Width for the Tk window.
    h = 600 # Height for the Tk window.

    ws = aboutWindow.winfo_screenwidth() # Width of the screen.
    hs = aboutWindow.winfo_screenheight() # Height of the screen.

    # X and Y coordinates for the Tk window.
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Dimensions of the screen and where it is placed.
    aboutWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Window background color
    aboutWindow.configure(bg = "white")

    "------------------------------------------------------"

    # Application description ---------------------------- #
    aboutLabel = Label(aboutWindow, text = "About application",
        bg = "white",
        font = ("Courier New", 11)
    )
    aboutLabel.pack(
        side = TOP,
        padx = 10,
        pady = (10, 0)
    )

    # Close application description window --------------- #
    closeButton = Button(aboutWindow, text = "Close",
        bg = "white",
        relief = SOLID,
        font = ("Courier New", 12),
        command = lambda: close(aboutWindow)
    )
    closeButton.pack(
        side = BOTTOM,
        pady = (10, 10),
        ipadx = 61,
        ipady = 5
    )

    "------------------------------------------------------"

    # Window MainLoop
    aboutWindow.mainloop()

def randomChoice(self): # From the previously selected folder, list all the subfolders there are and choose a random one.
    try:
        movieFolder = os.listdir(xFolder)
        for x in range(1):
            movieResult = random.choice(movieFolder)
            self.displayResultLabel.config(text = movieResult)
    except FileNotFoundError:
        selectFolder(self)

def playChoice(self): # Open the movie's folder and list all the files inside.
    print("Play selected movie")