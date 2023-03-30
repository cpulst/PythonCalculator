##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## GUI module. GUI.py manages the main gui object and calls the GUI CRUD functions as needed to change the interface
##
## Dependencies: ******Maybe create, read, update, delete

# Imports
import tkinter as tk
from guiCreate import *
from guiEventHandler import *

# Power class
class GUI:
    # Initialize Class
    def __init__(self):
        pass
    
    def createWindow(self):
        self.window = CreateGui()
        self.window.createWindow()
        
    # Test
    def test(self, msg):
        print("GUI Mod", msg)

newGui = GUI()
newGui.createWindow()

