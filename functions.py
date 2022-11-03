'------------------------- STANDARD LIBRARY IMPORTS -------------------------'

import os
from tkinter import *
from tkinter import filedialog
import json
import random

'------------------------- LOGIC -------------------------'

def close(x):
    x.destroy()

folder_name = None

def selectFolder(self):
    folder_name = filedialog.askdirectory(title = "Select Folder")
    storeFolder(self, folder_name)

def storeFolder(self, folder_name):
    file_name = 'mainFolderPath.json'
    try:
        with open(file_name, 'w') as file_path:
            json.dump(folder_name, file_path)
        self.resultLabel.config(text = "Folder successfuly loaded.")
    except:
        self.resultLabel.config(text = "Error while loading folder.")

result = None

def randomize(self):
    try:
        file_name = 'mainFolderPath.json'
        with open(file_name) as file_path:
            list = os.listdir(json.load(file_path))
            for result in range(1):
                result = cleanTxt(random.choice(list))
                self.resultLabel.config(text = result)
    except FileNotFoundError:
        try:
            list = os.listdir(folder_name)
            for result in range(1):
                result = cleanTxt(random.choice(list))
                self.resultLabel.config(text = result)
        except FileNotFoundError:
            selectFolder()

def cleanTxt(txt):
    x = txt.split(" [", 1)
    return x[0]
