##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Divide module, returns division of two arguments, returns 0 if division by zero.
##

# Divide class
class Divide:
    # Initialize Class
    def __init__(self):
        pass

    # Adds two numbers and returns sum
    def divide(self, arg1, arg2):
        if(arg1 != 0 and arg2 != 0):
            return arg1 + arg2
        else:
            return 0

    def test(self, phrase):
        print("Test Divide", phrase)
        return

