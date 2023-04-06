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

    # Divides two numbers and returns division
    def divide(self, arg1, arg2):
        if(arg2 != 0):
            return round(int(arg1) / int(arg2), 4)
        else:
            return 0

    def test(self, phrase):
        print("Test Divide", phrase)
        return

