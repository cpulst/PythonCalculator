##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Error handling module. Takes an error code, processes the appropriate response, prints error 
## and human readable test to console, informs user if necessary
##

## NH: I think there is a way to use and extend the built in error handling, that would be a better way of implementing your own


# Error class
class Error():
    # Initialize Class
    def __init__(self, error):
        pass

    # Switcher, figures out what type of error and calls custom
        
    # Prints error to console
    def throwError(self, error, errorCode=0, message=""):
        print("ERROR:", str(errorCode), message)
    
    
    # Updates user with error message on UI

