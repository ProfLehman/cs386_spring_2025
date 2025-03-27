# -----------------------------------------------
#     Program: basics_update_label_dialog.py
#
#      Author: Prof. Lehman
#
#        Date: 17 January 2025
#
# Description: This Tkinter application displays a label with a bold Arial font (size 24) and a button.
#             - Pressing the button opens a dialog box prompting the user to enter a new word.
#             - The entered word is then displayed in the label.
#             - Demonstrates user input handling with dialog boxes in Tkinter.
#             - Demonstrates messagebox
#

import tkinter as tk
from tkinter import simpledialog, messagebox

def update_label():
    new_word = simpledialog.askstring("Input", "Enter a new word:")

    if new_word:
        label.config(text=new_word)
    else:
        messagebox.showwarning("Warning", "Noting updated\nPlease Enter a word to update")

# Create the main window
root = tk.Tk()
root.title("Basics - Update Label with Dialog")
root.geometry("400x200")

# Create a Label widget with Arial 24 bold font
label = tk.Label(root, text="Hello", font=("Arial", 24, "bold"))
label.pack(pady=20)

# Create a Button to update the label
update_button = tk.Button(root, text="Update Word", command=update_label)
update_button.pack(pady=10)

# Run the application
root.mainloop()
