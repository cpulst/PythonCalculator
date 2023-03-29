##
## Author: Christopher Pulst
## Date: 3/28/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Create GUI module. Creates a gui interface and binds button actions
##

import tkinter as tk

# Power class
class CreateGui:
    # Initialize Class
    def __init__(self):
        self.root = tk.Tk()
        
        # Defaults
        self.bgColor = "#4A4A4A"
        self.minSize = (400, 600)
        self.maxSize = None
        
        pass
    
    # Create initial window
    def createWindow(self, width=200, height=200):
        print("createwindow")
        self.root.title("hello world")
        self.root.configure(background = self.bgColor)
        self.root.display = tk.Text(self.root, width=200, height=10)
        
        # Number Buttons
        self.root.btn0 = tk.Button(self.root, text="0", command=lambda:self.buttonPress(0))
        self.root.btn1 = tk.Button(self.root, text="1", command=lambda:self.buttonPress(1))
        self.root.btn2 = tk.Button(self.root, text="2", command=lambda:self.buttonPress(2))
        self.root.btn3 = tk.Button(self.root, text="3", command=lambda:self.buttonPress(3))
        self.root.btn4 = tk.Button(self.root, text="4", command=lambda:self.buttonPress(4))
        self.root.btn5 = tk.Button(self.root, text="5", command=lambda:self.buttonPress(5))
        self.root.btn6 = tk.Button(self.root, text="6", command=lambda:self.buttonPress(6))
        self.root.btn7 = tk.Button(self.root, text="7", command=lambda:self.buttonPress(7))
        self.root.btn8 = tk.Button(self.root, text="8", command=lambda:self.buttonPress(8))
        self.root.btn9 = tk.Button(self.root, text="9", command=lambda:self.buttonPress(9))
        
        # Operator Buttons
        self.root.btnEqual = tk.Button(self.root, text="=", command=lambda:self.buttonPress("="))
        self.root.btnPower = tk.Button(self.root, text="^", command=lambda:self.buttonPress("^"))
        self.root.btnDivide = tk.Button(self.root, text="/", command=lambda:self.buttonPress("/"))
        self.root.btnMultiply = tk.Button(self.root, text="*", command=lambda:self.buttonPress("*"))
        self.root.btnAdd = tk.Button(self.root, text="*", command=lambda:self.buttonPress("+"))
        self.root.btnSubtract = tk.Button(self.root, text="*", command=lambda:self.buttonPress("*"))
        
        # State Buttons
        self.root.btnSave = tk.Button(self.root, text="Save", command=lambda:self.buttonPress("save"))
        self.root.btnReset = tk.Button(self.root, text="Reset", command=lambda:self.buttonPress("reset"))
        self.root.btnClear = tk.Button(self.root, text="Clear", command=lambda:self.buttonPress("clear"))
        
        self.root.btn0.pack(side="left")
        self.root.btn1.pack(side="left")
        self.root.btn2.pack(side="left")
        self.root.btn3.pack(side="left")
        self.root.btn4.pack(side="left")
        self.root.btn5.pack(side="left")
        self.root.btn6.pack(side="left")
        self.root.btn7.pack(side="left")
        self.root.btn8.pack(side="left")
        self.root.btn9.pack(side="left")
        
        self.root.btnEqual.pack(side="left")
        self.root.btnPower.pack(side="left")
        self.root.btnDivide.pack(side="left")
        self.root.btnMultiply.pack(side="left")
        self.root.btnAdd.pack(side="left")
        self.root.btnSubtract.pack(side="left")
        
        self.root.btnSave.pack(side="left")
        self.root.btnClear.pack(side="left")
        self.root.btnReset.pack(side="left")
        
        print("end create window")
        self.root.mainloop()
        return self.root

    # Button press capture
    def buttonPress(self, operator, *args):
        if(operator == "clear"):
            print("clear")
        if(operator == "/"):
            print("division")
        if(operator == "/"):
            print("division")
        if(operator == "*"):
            print("multipy")
        if(operator == "^"):
            print("power")
        if(operator == "+"):
            print("addition")
        if(operator == "-"):
            print("subtraction")
        print("button pressed",args)
        return 
    
    # Test
    def test(self, msg):
        print("GUI create Mod", msg)
