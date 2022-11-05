# ------------------------- Standard Library Imports ------------------------- #

import tkinter as tk
from tkinter import *

# ------------------------- Local Imports ------------------------- #

from gui import mainWindow

# ------------------------- Logic ------------------------- #

def main():
    root = tk.Tk
    mainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()