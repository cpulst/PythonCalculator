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
import modules.ui.guiCreate as ui

# Main function
def main():
    window = ui.CreateGui()
    window.createWindow()
    
main()