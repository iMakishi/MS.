'------------------------- STANDARD LIBRARY IMPORTS -------------------------'

from tkinter import *

'------------------------- LOCAL IMPORTS -------------------------'

from functions import close
from functions import selectFolder
from functions import randomize

'------------------------- LOGIC -------------------------'

class MainWindow:
    def __init__(self, master):
        self.master = master

        '--------------------------------------------------'

        # Window bar
        master.title('MOVIƎ RAN|SEL')
        master.resizable(0, 0)

        # Window size and position
        window_width = 925 # Width for the Tk window.
        window_height = 310 # Height for the Tk window.

        screen_width = master.winfo_screenwidth() # Width of the screen.
        screen_height = master.winfo_screenheight() # Height of the screen.

        # X and Y coordinates for the Tk window.
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)

        # Dimensions of the screen and where it is placed.
        master.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        # Window background color
        master.configure(bg = 'white')

        '--------------------------------------------------'

        # Menubar
        menubar = Menu(master,
                       bg = 'white',
                       activebackground = 'white',
                       relief = FLAT,
                       borderwidth = 0)

        master.config(menu = menubar)

        '--------------------------------------------------'

        # File Section (Menubar)
        filemenu = Menu(menubar,
                        tearoff = 0,
                        relief = FLAT)

        menubar.add_cascade(label = "File",
                            menu = filemenu)

        # # Select Folder (File Section (Menubar))
        filemenu.add_command(label = "Select Folder...  ",
                             command = lambda: selectFolder(self))

        # # Preferences (File Section (Menubar))
        preferences_submenu = Menu(filemenu,
                                   tearoff = 0,
                                   relief = FLAT)

        filemenu.add_cascade(label = "Preferences",
                             menu = preferences_submenu)

        # # # Filter (Preferences (File Section (Menubar)))
        preferences_submenu.add_command(label = "Filters",
                                        command = None)

        # # Quit (File Section (Menubar))
        filemenu.add_separator()
        filemenu.add_command(label = "Quit",
                             command = lambda: close(master))

        '--------------------------------------------------'

        # Help Section (Menubar)
        helpmenu = Menu(menubar,
                        tearoff = 0)

        menubar.add_cascade(label = "Help",
                            menu = helpmenu)

        # # Release Notes (Help Section (Menubar))
        helpmenu.add_command(label = "Release Notes",
                             command = None)

        # # Report Problem (Help Section (Menubar))
        helpmenu.add_command(label = "Report a problem",
                             command = None)

        # # About (Help Section (Menubar))
        helpmenu.add_separator()
        helpmenu.add_command(label = "About",
                             command = None)

        '--------------------------------------------------'

        # Main Window Frame Sections Content

        '------------------------- Top Frame Section -------------------------'
        TopFrame = Frame(master,
                         bg = 'white')

        TopFrame.pack(ipadx = window_width)

        internalTopFrame = Frame(TopFrame,
                                 bg = 'white')

        internalTopFrame.pack(side = TOP,
                              ipadx = window_width)

        # Filters Button (Superior Top Frame Section)
        filtersButton = Button(internalTopFrame,
                               text = "Filters",
                               font = ('Overpass', 12, 'bold'),
                               bg = 'white',
                               activebackground = 'white',
                               relief = FLAT,
                               borderwidth = 0,
                               highlightthickness = 0,
                               command = None)

        filtersButton.pack(side = TOP,
                           anchor = NE,
                           padx = 10)

        # App Title (Inferior Top Frame Section)
        appTitle = Label(internalTopFrame,
                         text = " MOVIE RANSEL ",
                         font = ('Overpass', 24, 'italic bold underline'),
                         bg = 'white')

        appTitle.pack(side = BOTTOM)

        # Result Label
        self.resultLabel = Label(TopFrame,
                            text = ". . .",
                            font = ('Overpass', 14, 'bold'),
                            bg = 'white',)

        self.resultLabel.pack(side = BOTTOM,
                         padx = 10,
                         pady = 5,
                         ipadx = window_width,)

        '------------------------- Middle Frame Section -------------------------'

        MiddleFrame = Frame(master,
                            bg = 'white')

        MiddleFrame.pack(ipadx = window_width)

        # Full Index Button
        indexButton = Button(MiddleFrame,
                             text = "Index",
                             font = ('Overpass', 12, 'bold'),
                             relief = SOLID,
                             bg = 'white',
                             activebackground = 'white',
                             command = None)

        indexButton.pack(side = LEFT,
                         padx = (242, 5),
                         pady = (10, 10))

        indexButton.config(width = 20)

        # Randomize Button
        randomizeButton = Button(MiddleFrame,
                                 text = "Randomize",
                                 font = ('Overpass', 12, 'bold'),
                                 relief = SOLID,
                                 bg = 'white',
                                 activebackground = 'white',
                                 command = lambda: randomize(self))

        randomizeButton.pack(side = RIGHT,
                             padx = (5, 242),
                             pady = (10, 10))

        randomizeButton.config(width = 20)

        '------------------------- Bottom Frame Section -------------------------'

        BottomFrame = Frame(master,
                            bg = 'white')

        BottomFrame.pack(ipadx = window_width)

        # Exit Button
        exitButton = Button(BottomFrame,
                            text = "Exit",
                            font = ('Overpass', 12, 'bold'),
                            relief = SOLID,
                            bg = 'white',
                            activebackground = 'white',
                            command = lambda: close(master))

        exitButton.pack(side = TOP,
                        pady = (10, 10))

        exitButton.config(width = 20)

        # Signature Label
        signatureLabel = Label(BottomFrame,
                               text = "@2022 by iMakishi. (Maximiliano E. Lutz)",
                               font = ('Overpass', 10, 'bold'),
                               bg = 'white')

        signatureLabel.pack(side = BOTTOM,
                            ipady = 5)
        
    def FiltersWindow(self):
        self.FiltersWindow = Toplevel(self.master)

'--------------------------------------------------'

class FiltersWindow:
    pass

'--------------------------------------------------'

class IndexWindow:
    pass

'--------------------------------------------------'

class SettingsWindow:
    pass

'--------------------------------------------------'

class ReleaseNotesWindow:
    pass

'--------------------------------------------------'

class ReportProblemWindow:
    pass

'--------------------------------------------------'

class AboutWindow:
    pass