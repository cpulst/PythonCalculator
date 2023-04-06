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


#import sys
#import os

#projectRoot = os.path.abspath(os.curdir)
#sys.path.append(projectRoot + "\\modules\\mathCustom")
#print(sys.path)

import tkinter as tk


import sys
import os

current = os.path.dirname(os.path.realpath(__file__)) 
parent = os.path.dirname(current)
sys.path.append(parent)

from mathCustom import *


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

        #Event Variables
        self.num1 = None
        self.num2 = None
        self.operator = None
        self.result = None
        self.rowId = None
    
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

    # Add number to textbox given value
    def addNumber(self, val):
        self.textbox["text"] = val
        
    
    def calculateResult(self):
        if self.operator == "+":
            add = addition.Addition()
            return add.add(self.num1, self.num2)
        if self.operator == "-":
            subtract = subtraction.Subtraction()
            return subtract.subtract(self.num1, self.num2)
        if self.operator == "/":
            quotient = divide.Divide()
            return quotient.divide(self.num1,self.num2)
        if self.operator == "*":
            product = multiply.Multiply()
            return product.multiply(self.num1, self.num2)
        if self.operator == "^":
            exponent = power.Power()
            exponent.power(self.num1, self.num2)
        else:
            return "Error"

    # Button Press Handler
    def buttonPress(self, val):
        
        # Catch numerical input
        if isinstance(val,int) and 0 <= val <= 9:
            # Convert to string for concatination
            val = str(val)
            
            
            # set num1 variable for first time
            if self.num1 == None:
                self.num1 = val
                self.addNumber(self.num1)
                return
            
            # concat num1 if value exists
            if self.num1 != None and self.operator == None:
                self.num1 = self.num1 + val
                self.addNumber(self.num1)
                return
            
            # set num2 value for first time if operator has been pressed
            if self.num2 == None and self.operator != None:
                self.num2 = val
                self.addNumber(self.num2)
                return
            
            # concat num2 value if num2 value and operator value exist
            if self.num2 != None and self.operator != None:
                self.num2 = self.num2 + val
                self.addNumber(self.num2)
                return
        
        # Catch operator input
        if val == "+" or val == "-" or val == "*" or val == "/" or val == "^":
            
            # set operator value for first time
            if self.operator == None:
                self.operator = val
                self.addNumber(self.operator)
                return
            
            # calculate result and log equation if second operator is pressed and num2 val exists
            if self.operator != None and self.num2 != None:
                
                print("Here goes call to calculate result")
                self.addNumber(self.operator)
                # Calculate the result of the operation, log database, update user of result, store answer in num1, return num2 to None
                return

            # Error catching for two operators pressed in a row, alternatively, could replace operator allowing user to change selected operation
            if self.operator != None and self.num2 == None:
                print("error, second value must be entered before another operator can be used")
                self.addNumber(self.operator)
                return
            
        # Catch equals input
        if val == "=":

            # Validate 
            if self.num1 != None and self.num2 != None:

                # Calc result, store answer, send equation and result to db
                print("Calculate the result of the equation")
                self.result = self.calculateResult()
                self.addNumber(self.result)                
            return
        
        # Catch history state up input
        if val == "up":
            # Will need to validate if the user is currently looking at history state
            # if no - canvas DB, read last entry, construct string, present equation to user
            # if yes - validate row is not first row, if yes, do nothing, if no decrement row id val
            # call DB, read row values, construct string, present to user
            print("call database, show next row up")
            return

        # Catch history state down input
        if val == "down":
            # Will need to validate if the user is currently looking at history state
            # if yes - validate row is not last row, if yes, do reset calculator to defaults, if no increment row id val
            # call DB, read row values, construct string, present to user
            print("call database, show next row down")
            return

        # Catch clear current value input
        if val == "c":
            # validat if num2, operator, or num1 was last change (check for None)
            # return the last changed variable to None
            if self.num1 != None:
                if self.operator != None:
                    if self.num2 != None:
                        self.num2 = None
                        self.addNumber(0)
                    else:
                        self.operator = None
                        self.addNumber(0)
                else:
                    self.num1 = None
                    self.addNumber(0)
            else:
                self.addNumber(0)
            print("Clear current")
            return
        
        # Catch reset all input
        if val == "reset":
            self.result = None
            self.num1 = None
            self.num2 = None
            self.operator = None
            self.rowId = None
            self.addNumber(0) 
            # Call DB, remove all entries
            # reset num1, num2, operator, result, rowId to None
            # Update UI to default state
            print("reset pressed")
            return
