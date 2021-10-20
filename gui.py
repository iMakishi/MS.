# Imports

import tkinter as tk
from tkinter import *
import os
import random

# Import main.py Definitions

from main import selectFolder
from main import customizeAppearance
from main import customizeSettings

from main import releaseNotes
from main import reportProblem
from main import appAbout

from main import randomChoice
from main import playChoice

# MAIN

class GUI:
    def __init__(self, master):
        self.master = master

        "--------------------------------------------------"

        # Window bar
        master.title("!MS.")
        master.resizable(0, 0)

        # Window size and position
        w = 900 # Width for the Tk window.
        h = 250 # Height for the Tk window.

        ws = master.winfo_screenwidth() # Width of the screen.
        hs = master.winfo_screenheight() # Height of the screen.

        # X and Y coordinates for the Tk window.
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # Dimensions of the screen and where it is placed.
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Window background color
        master.configure(bg = "white")

        "--------------------------------------------------"

        # MAIN Bar
        menubar = Menu(master)
        master.config(menu = menubar)

        "--------------------------------------------------"

        # File Section
        filemenu = Menu(menubar,
            tearoff = 0
        )
        menubar.add_cascade(label = "File",
            menu = filemenu
        )

        # File Section ---> Folder selection
        filemenu.add_command(label = "Select Folder...      ",
            command = lambda: selectFolder(self)
        )

        # File Section ---> Preferences
        preferences_submenu = Menu(filemenu,
            tearoff = 0
        )
        filemenu.add_cascade(label = "Preferences",
            menu = preferences_submenu
        )

        # File Section ---> Preferences ---> Appearance
        preferences_submenu.add_command(label = "Appearance",
            command = lambda: customizeAppearance(self)
        )

        # File Section ---> Preferences ---> Settings
        preferences_submenu.add_command(label = "Settings",
            command = lambda: customizeSettings(self)
        )

        # File Section ---> Quit
        filemenu.add_separator()
        filemenu.add_command(label = "Quit",
            command = master.quit
        )

        "--------------------------------------------------"

        # Help Section
        helpmenu = Menu(menubar,
            tearoff = 0
        )
        menubar.add_cascade(label = "Help",
            menu = helpmenu
        )

        # Help Section ---> Release Notes
        helpmenu.add_command(label = "Release Notes",
            command = lambda: releaseNotes(self)
        )

        # Help Section ---> Report a problem
        helpmenu.add_command(label = "Report a problem",
            command = lambda: reportProblem(self)
        )

        # Help Section ---> About
        helpmenu.add_separator()
        helpmenu.add_command(label = "About",
            command = lambda: appAbout(self)
        )

        "--------------------------------------------------"

        " MAIN Window "

        " Top Frame ---------------------------------------"

        self.topFrame = Frame(master, bg = "white")
        self.topFrame.pack()

        # Application title ------------------------------ #
        self.appTitleLabel = Label(self.topFrame, text = " !MoviƎSElecT. ",
            bg = "white",
            font = ("Courier New", 30, "underline")
        )
        self.appTitleLabel.pack(
            side = TOP,
            pady = 5,
            ipadx = 250
        )

        # Display random movie choice result. ------------ #
        self.displayResultLabel = Label(self.topFrame, text = "",
            bg = "white",
            font = ("Courier New", 15, "bold")
        )
        self.displayResultLabel.pack(
            side = BOTTOM,
            pady = 5,
            ipadx = 5
        )

        " Middle Frame ------------------------------------"

        self.middleFrame = Frame(master, bg = "white")
        self.middleFrame.pack()

        # Randomize button ------------------------------- #
        self.randomizeButton = Button(self.middleFrame, text = "Randomize",
            bg = "white",
            relief = SOLID,
            font = ("Courier New", 12),
            command = lambda: randomChoice(self)
        )
        self.randomizeButton.pack(
            side = LEFT,
            padx = (0, 5),
            pady = (15, 0),
            ipadx = 40,
            ipady = 5
        )

        # Play button ------------------------------------ #
        self.playButton = Button(self.middleFrame, text = "Play",
            bg = "white",
            relief = SOLID,
            font = ("Courier New", 12),
            command = lambda: playChoice(self)
        )
        self.playButton.pack(
            side = RIGHT,
            padx = (5, 0),
            pady = (15, 0),
            ipadx = 60,
            ipady = 5
        )

        " Bottom Frame ------------------------------------"

        self.bottomFrame = Frame(master, bg = "white")
        self.bottomFrame.pack()

        # Exit button ------------------------------------ #
        self.exitButton = Button(self.bottomFrame, text = "Exit",
            bg = "white",
            relief = SOLID,
            font = ("Courier New", 12),
            command = lambda: exit()
        )
        self.exitButton.pack(
            side = TOP,
            pady = (10, 10),
            ipadx = 61,
            ipady = 5
        )

        # License label ---------------------------------- #
        self.licenseLabel = Label(self.bottomFrame, text = "@2021 by Maximiliano E. Lutz",
            bg = "white",
            font = ("Courier New", 10, "underline")
        )
        self.licenseLabel.pack(
            side = BOTTOM,
            pady = 5,
            ipady = 5
        )

        "--------------------------------------------------"

# Program Execution

if __name__ == '__main__':
    root = Tk()
    AppGui = GUI(root)
    root.mainloop()