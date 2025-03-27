import tkinter as tk

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

class Form2:
    def __init__(self, parent):
        
        # store reference to calling form
        self.parent = parent
        
        # create GUI for form2
        self.window = tk.Tk()
        self.window.title("Form 2")
        self.window.geometry("300x200")
        
        tk.Label(self.window, text="Enter Text:", font=("Arial", 12)).pack(pady=10)

        self.text_entry = tk.Entry(self.window, font=("Arial", 12))
        self.text_entry.pack(pady=5)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        submit_btn = tk.Button(btn_frame, text="Submit", command=self.submit_text)
        submit_btn.grid(row=0, column=0, padx=5)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.window.destroy)
        cancel_btn.grid(row=0, column=1, padx=5)

        self.window.mainloop()
        
    def submit_text(self):
        self.parent.label.config(text=self.text_entry.get())
        #self.window.destroy()
