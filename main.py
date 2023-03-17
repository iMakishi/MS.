# ------------------------- Standard Library Imports ------------------------- #

import sys
from PyQt5.QtWidgets import QApplication

# ------------------------- Local Imports ------------------------- #

from gui import mainWindow

# ------------------------- Logic ------------------------- #

def main():
    app = QApplication(sys.argv)
    myApp = mainWindow()
    myApp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
