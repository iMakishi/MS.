'------------------------- STANDARD LIBRARY IMPORTS -------------------------'

import os
from tkinter import *
from tkinter import filedialog
import json
import random


'------------------------- LOCAL IMPORTS -------------------------'



'------------------------- LOGIC -------------------------'

def close(x):
    x.destroy()

folder_name = ""

def selectFolder():
    global folder_name
    folder_name = filedialog.askdirectory(title = "Select Folder")
    storeFolder(folder_name)

def storeFolder(folder_name):
    file_name = 'path.json'
    try:
        with open(file_name, 'w') as file_path:
            json.dump(folder_name, file_path)
        print("Folder Saved ---> COMPLETE")
    except:
        print("Folder Saved ---> FAILED") 

result = ""

def randomize(self):
    try:
        file_name = 'path.json'
        with open(file_name) as file_path:
            list = os.listdir(json.load(file_path))
            for result in range(1):
                result = random.choice(list)
                self.resultLabel.config(text = result)
    except FileNotFoundError:
        try:
            list = os.listdir(folder_name)
            for result in range(1):
                result = random.choice(list)
                self.resultLabel.config(text = result)
        except FileNotFoundError:
            selectFolder()