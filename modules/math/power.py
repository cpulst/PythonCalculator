##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## power module. Utilizing the math python library, calculates and returns the exponent of a number given 
##
## Dependencies: Python Math module

# Imports
from math import pow

# Power class
class Power:
    # Initialize Class
    def __init__(self):
        pass

    # Calculate power
    def power(self, number, exp):
        return pow(number, exp)
    
    # Test
    def test(self, message):
        print("Power test", message)