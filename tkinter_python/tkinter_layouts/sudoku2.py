# sudoku2.py
#
# spring 2025
# prof. lehman
#
# demonstrates dynammic widgets
#
# code modifed from Chat GPT 4o prompt
#
#  Create a tkinter GUI with no functionality that displays a sudoku board
#  using Entry widgets that can store a number 0 to 9.  Make the font for
#  the Entry 18pt font.  Add a File menu with New and Exit options.
#  Make the new and exit option functional.  Place sample numbers on the board.
# 
# adjusted spacing using prompt
#  Given attached file, adjust spacing so that Entries are shown in typical
#  sudoku order as 9 groupings of 9 entries.
#
# manually added random numbers, set starting entries to blanks
#

import tkinter as tk
from tkinter import Menu
import random

def new_game():
    """Clear the Sudoku board."""
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, random.randint(0, 9))

def exit_game():
    """Exit the application."""
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Sudoku")

# Create a menu bar with a File menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_game)
file_menu.add_command(label="Exit", command=exit_game)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Create a frame for the Sudoku board
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entries = []  # Store all Entry widgets

# Create the Sudoku board using Entry widgets
for i in range(9):
    row_entries = []
    for j in range(9):
        padx = 2 if j % 3 == 2 and j != 8 else 1
        pady = 2 if i % 3 == 2 and i != 8 else 1
        entry = tk.Entry(frame, width=2, font=("Helvetica", 18), justify="center")
        entry.grid(row=i, column=j, padx=(5 if j % 3 == 0 else padx, padx), pady=(5 if i % 3 == 0 else pady, pady))
        #entry.config(state="disabled")
        row_entries.append(entry)
    entries.append(row_entries)

# Run the application
root.mainloop()
