# ------------------------- Standard Library Imports ------------------------- #

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction
from PyQt5.QtGui import QIcon

# ------------------------- Local Imports ------------------------- #



# ------------------------- Logic ------------------------- #

class mainWindow(QMainWindow, QWidget):
    # Class description ------------------------- #
    "App main grafical user interface."
    # ------------------------- #
    def __init__(self):
        super().__init__()
        self.title = "RAN/SEL"
        self.width = 720
        self.height = 480
        self.UI()

    def UI(self):       
        # Window Properties
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # Window Style
        
        css = """
            background-color: #ffffff;
            border-radius: 10px;
        """
        self.setStyleSheet(css)
        
        # Menubar
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        
        # Menubar Actions
        
        open_folder = QAction("Open Folder...", self)
        file_menu.addAction(open_folder)
        
        exit_action = QAction("Exit", self)
        file_menu.addAction(exit_action)
