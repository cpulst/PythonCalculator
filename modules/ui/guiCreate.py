##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Create GUI module. Creates a gui interface and binds button actions
##

import tkinter as tk
from guiEventHandler import *

# Power class
class CreateGui:
    # Initialize Class
    def __init__(self):
        # Window defaults
        self.root = tk.Tk()
        self.title="Calculator"
        self.windowSize = "250x300"
        self.resizable = (False,False)
        
        # Colors
        self.btnColor = "#4a4a4a"
        self.bgColor = "#282828"
        self.btnAltColor = "#588F9A"
        self.btnAccent = "#00FFA3"
        self.textAreaColor = "#CECECE"
        self.lightTextColor = "#FFFFFF"
        
        # Button values
        self.btnSize = (50,50)
        self.btns = [0,1,2,3,4,5,6,7,8,9]
        self.operators = ["c","reset","+","-","*","^","="]
    
    def createButtons(self):
        # increment values
        yVal = 1
        opIndex = 0

        # Create display label
        self.textbox = tk.Label(text=0,anchor="e",padx=15, bg=self.textAreaColor, font=("Helvetica", 22, "normal"))
        self.textbox.place(x=0, y=0, width=self.btnSize[0]*5, height=self.btnSize[1])

        # Create buttons
        for index, button in enumerate(self.btns):
            text = button
            
            # convert int to strings
            if type(button) == int:
                text = str(button)
            
            # handle 0 key, =, and history state keys
            if button == 0:
                
                # Create 0 key
                item = tk.Button(self.root, text=text, bd=0, bg=self.btnColor, fg=self.lightTextColor, command=lambda val=text:self.buttonPress(val))
                item.place(x=0, y=(self.btnSize[1] * 4), width=self.btnSize[0]*3, height=self.btnSize[1])
                
                # create equals key
                optBtn1 = tk.Button(self.root, text=self.operators[-1], bd=0, bg=self.btnAccent, command=lambda val=self.operators[-1]:self.buttonPress(val))
                optBtn1.place(x=0 + (self.btnSize[0] * 3), y=0 + (self.btnSize[1] * 4), width=self.btnSize[0] * 2, height=self.btnSize[1])

                # Create up history state key
                historyBtnUp = tk.Button(self.root, text=u"\u21E7", bd=0, bg=self.btnAltColor, command=lambda val="up":self.buttonPress(val))
                historyBtnUp.place(x=0, y=0 + (self.btnSize[1] * 5), width=self.btnSize[0] * 2.5, height=self.btnSize[1])

                # Create down history state key
                historyBtnDown = tk.Button(self.root, text=u"\u21E9", bd=0, bg=self.btnAltColor, command=lambda val="down":self.buttonPress(val))
                historyBtnDown.place(x=self.btnSize[0] * 2.5, y=0 + (self.btnSize[1] * 5), width=self.btnSize[0] * 2.5, height=self.btnSize[1])
            
            # create all other keys
            else:
                # define x position value
                xVal = (index-1)%3

                # Create button from array value
                item = tk.Button(self.root, text=text, bd=0, bg=self.btnColor, fg=self.lightTextColor, command=lambda val=text:self.buttonPress(val))
                item.place(x=0 + (self.btnSize[0] * xVal), y=0 + (self.btnSize[1] * yVal), width=self.btnSize[0], height=self.btnSize[1])

                # catch end of layout row condition
                if xVal==2:
                    
                    # select operator from array
                    operator = self.operators[opIndex]

                    # Create first right hand operator button
                    optBtn1 = tk.Button(self.root, text=operator, bd=0, bg=self.btnAccent, command=lambda val=operator:self.buttonPress(val))
                    optBtn1.place(x=0 + (self.btnSize[0] * 3), y=0 + (self.btnSize[1] * yVal), width=self.btnSize[0], height=self.btnSize[1])
                    opIndex += 1

                    # Create second right hand operator button
                    operator = self.operators[opIndex]
                    optBtn2 = tk.Button(self.root, text=operator, bd=0, bg=self.btnAccent, command=lambda val=operator:self.buttonPress(val))
                    optBtn2.place(x=0 + (self.btnSize[0] * 4), y=0 + (self.btnSize[1] * yVal), width=self.btnSize[0], height=self.btnSize[1])
                    
                    # increment operator and yVal index
                    opIndex += 1
                    yVal += 1
    
    # Create initial window
    def createWindow(self):
        
        # Create window
        self.root.geometry(self.windowSize)
        self.root.title(self.title)
        self.root.configure(background = self.bgColor)
        self.root.resizable(self.resizable[0], self.resizable[1])
        
        # Create buttons
        self.createButtons()
        
        # Initialize tkinter main loop
        self.root.mainloop()
        return self.root

    # Button press capture
    def buttonPress(self, val):
        
        if 0 <= int(val) <= 9:
            event = Event()
            event.buttonPress(val,self.textbox)
        if(val == "clear"):
            print("clear")
        if(val == "/"):
            print("division")
        if(val == "/"):
            print("division")
        if(val == "*"):
            print("multipy")
        if(val == "^"):
            print("power")
        if(val == "+"):
            print("addition")
        if(val == "-"):
            print("subtraction")
        print("button pressed",val)
        return 
    
    # Test
    def test(self, msg):
        print("GUI create Mod", msg)
