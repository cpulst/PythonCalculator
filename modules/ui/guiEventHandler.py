##
## Author: Christopher Pulst
## Date: 3/29/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Captures UI button presses and handles operations
##
## Dependencies: 
## Math directory scripts
##

#from math.addition import *
#from math.divide import *
#from math.multiply import *
#from math.power import *
#from math.subtraction import *
from guiUpdate import *

class Event:
    def __init__(self, textbox):
        self.num1 = None
        self.num2 = None
        self.operator = None
        self.result = None
        self.rowId = None
        self.textbox = textbox
        
        pass
    
    # Add number to textbox given value
    def addNumber(self, value):
        self.textbox.config(text = value)
    
    def buttonPress(self, val, root):
        
        # Catch numerical input
        if 0 <= int(val) <= 9:
            # Convert to string for concatination
            val = str(val)
            #self.update = UIUpdate(root)
            #self.update.addNumber(self,val)
            self.addNumber(self,val)
            
            # set num1 variable for first time
            if self.num1 == None:
                self.num1 = val
                
                return
            
            # concat num1 if value exists
            if self.num1 != None and self.operator == None:
                self.num1 = self.num1 + val
                return
            
            # set num2 value for first time if operator has been pressed
            if self.num2 == None and self.operator != None:
                self.num2 = val
                return
            
            # concat num2 value if num2 value and operator value exist
            if self.num2 != None and self.operator != None:
                self.num2 = self.num2 + val
                return
        
        # Catch operator input
        if val == "+" or val == "-" or val == "*" or val == "/" or val == "^":
            
            # set operator value for first time
            if self.operator == None:
                self.operator = val
                return
            
            # calculate result and log equation if second operator is pressed and num2 val exists
            if self.operator != None and self.num2 != None:
                print("Here goes call to calculate result")
                # Calculate the result of the operation, log database, update user of result, store answer in num1, return num2 to None
                return

            # Error catching for two operators pressed in a row, alternatively, could replace operator allowing user to change selected operation
            if self.operator != None and self.num2 == None:
                print("error, second value must be entered before another operator can be used")
                return
            
        # Catch equals input
        if val == "=":

            # Validate 
            if self.num1 != None and self.num2 != None:

                # Calc result, store answer, send equation and result to db
                print("Calculate the result of the equation")
                
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
        if val == "clear":
            # validat if num2, operator, or num1 was last change (check for None)
            # return the last changed variable to None
            print("Clear current")
            return
        
        # Catch reset all input
        if val == "reset":
            # Call DB, remove all entries
            # reset num1, num2, operator, result, rowId to None
            # Update UI to default state
            print("reset pressed")
            return
