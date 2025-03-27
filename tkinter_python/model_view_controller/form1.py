import tkinter as tk
from form2 import *

# form2.py
# prof.  lehman
# spring 2025
#
# demonstrates sending data between forms
#
#  Form1 -> opens Form2( Form1 reference )
#
#        <- Form2 updates label in Form1 using Form1 reference
#

class Form1:
    def __init__(self):
        
        # create GUI
        self.root = tk.Tk()
        self.root.title("Form 1")
        self.root.geometry("300x200")
        
        self.label = tk.Label(self.root, text="Sample Text", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)
        
        self.open_form2_btn = tk.Button(self.root, text="Update Text", command=self.open_form2)
        self.open_form2_btn.pack(pady=10)
        
        self.root.mainloop()
        
    def open_form2(self):
        f2 = Form2(self) # create instance of Form2

if __name__ == "__main__":
    
    test = Form1()
    #test.root.mainloop()
