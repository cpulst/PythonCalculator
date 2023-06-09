##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Subtraction module, returns the difference of two numbers
##

# Subtraction class
class Subtraction:
    # Initialize Class
    def __init__(self):
        pass

    # Subtracts two numbers and returns the difference
    def subtract(self, arg1, arg2):
        return round(int(arg1) - int(arg2), 4)

    def test(self, phrase):
        print("Test subtraction", phrase)
        return

