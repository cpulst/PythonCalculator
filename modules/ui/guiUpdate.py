##
## Author: Christopher Pulst
## Date: 3/29/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Updates the textbox of the gui give input values
##

# Power class
class UIUpdate:
    # Initialize Class
    def __init__(self, root):
        if root != None:
            self.root = root
            
        else:
            print("error")
        pass

    # Reset textbox to 0
    def clearTextbox(self):
        self.textbox.config(text = 0)
    
    # Add number to textbox given value
    def addNumber(self, value):
        self.textbox.config(text = value)
    