
# dynamic_widgets.py
# spring 2025
# prof. lehman
# demonstrates dynamic widgets
#

import tkinter as tk
from tkinter import Menu
import random

def place_numbers():
    for i in range(9):
        entries[i].delete(0, tk.END)
        entries[i].insert(0, random.choice([" ",1,2,3,4,5,6]))

def exit_app():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("dynamic widgets")

# Create a menu bar with a File menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=place_numbers)
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Create a frame for widgets (rather than direct to root)
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entries = []  # Store all Entry widgets in list

# Create GUI dynamically
col = 0 #column placement of widget

i = 0 #number of widgets to place
labels = "ABCDEFGHIJ"

while i < 9:
    
    # add label (no reference kept)
    tk.Label( frame, text=labels[i],font=("Helvetica", 18) ).grid(row=0, column=col)
    col = col + 1
    
    # add entry (reference kept in entries list)
    entry = tk.Entry(frame, width=2, font=("Helvetica", 18, "bold"), justify="center")
    entry.grid(row=0, column=col, padx=8, pady=5)
    entries.append(entry)
    col = col + 1
    
    i = i + 1

print( entries ) #show list of widgets

# Run the application
root.mainloop()

