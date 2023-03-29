##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description
## -------------
## A calulator application with a GUI frontend that allows for basic math problems and storage of history in a database.
##
## Dependencies
## --------------
## addition.py
## divide.py
## error.py
## exponent.py
## gui.py
## multiply.py
## substraction.py
## database.py
## 

# Imports
from addition import *
from divide import *
from error import *
from power import *
from multiply import *
from subtraction import *
from database import *

# Main function
def main():
    print("hello world!")
    addTest = Addition()
    addTest.test("I fucking work!")
    
    divideTest = Divide()
    divideTest.test("I going to divide by zero if it kills me")
    
    error = Error("Error")
    error.throwError("test", 1, "Fuck me")
    
    power = Power()
    power.test("Hello Chris")
    
    multi = Multiply()
    multi.test("Do you feel bonita?")
    
    sub = Subtraction()
    sub.test("I feel bonita...")
    
    db = Database()
    db.test("DB for the win")
    
main()