'------------------------- STANDARD LIBRARY IMPORTS -------------------------'

from tkinter import *

'------------------------- LOCAL IMPORTS -------------------------'

from UI import MainWindow

'------------------------- LOGIC -------------------------'

if __name__ == '__main__':
    root = Tk()
    app = MainWindow(root)
    root.mainloop()