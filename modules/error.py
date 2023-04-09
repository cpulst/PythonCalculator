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

## I think there is a way to use and extend the built in error handling, that would be a better way

#print(sys.path)

class zeroDivison(Exception):
    def __init__(self):
        print("Halt! You violated the law...of mathmatics...")
        

class indexError(Exception):
    def __init__(self):
        print("Halt! You violated the law...of mathmatics...")
        

# Error class
class Error():
    # Initialize Class
    def __init__(self, error):
        pass

    # Switcher, figures out what type of error and calls custom
        """
        except ZeroDivisionError:
            print("ZeroDivisionError occured, cannot divide by zero")
        except IndexError:
            print("List index out of range")
        except SyntaxError:
            print("Syntax error occured")
        except TypeError:
            print("Invalid arguments given")       
        """
        
    
    
    
    # Updates user with error message on UI

