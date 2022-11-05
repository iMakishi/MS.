# ------------------------- Standard Library Imports ------------------------- #

import tkinter as tk
from tkinter import *

# ------------------------- Local Imports ------------------------- #



# ------------------------- Logic ------------------------- #

class mainWindow:
    # Class description ------------------------- #
    "App main grafical user interface."
    # ------------------------- #
    
    def __init__(self, master):
        self.master = master
        
        # Window bar
        master.title("RAN/SEL")
        master.resizable(0, 0)

        # Window size and position
        window_width = 720 # Width for the Tk window.
        window_height = 480 # Height for the Tk window.

        screen_width = master.winfo_screenwidth() # Width of the screen.
        screen_height = master.winfo_screenheight() # Height of the screen.

        # X and Y coordinates for the Tk window.
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)

        # Dimensions of the screen and where it is placed.
        master.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        # Window background color
        master.configure(bg = 'white')