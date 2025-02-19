# p5.py
# *** update your name here ***
# spring 2025
# shell for p5 assignment
#
# GUI demonstrates saving data as text, CSV, XML, JSON, binary, and object
#

import tkinter as tk
from tkinter import Menu

# *** To Do ***
# update each of the following functions to open/save data related to your project

def new_file():
    print("GUI Reset")
    textbox.delete(0, tk.END)   # Clear the textbox
    checkbox_var.set(False)     # Uncheck the checkbox
    radio_var.set("option1")    # Reset radio buttons to default value
    
def exit_app():
    print("Exit Application")
    root.destroy()

def open_text():
    print("Open Text file.")

def open_csv():
    print("Open CSV file.")

def open_xml():
    print("Open XML file.")

def open_json():
    print("Open JSON file.")

def open_binary():
    print("Open Binary file.")

def open_object():
    print("Open Object file.")

def save_text():
    print("Save Text file.")

def save_csv():
    print("Save CSV file.")
    
def save_xml():
    print("Save XML file.")

def save_json():
    print("Save JSON file.")

def save_binary():
    print("Save Binary file.")

def save_object():
    print("Save Object file.")


# --- Create GUI ---
root = tk.Tk()
root.title("CS 386 p5")
root.geometry("400x300")

# *** To Do ***
# add/update GUI components here

# Create a frame to hold additional widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# --- Textbox ---
# Here we use an Entry widget for a single-line textbox.
textbox = tk.Entry(frame, width=40)
textbox.pack(pady=5)

# --- Checkbox ---
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(frame, text="I agree", variable=checkbox_var)
checkbox.pack(pady=5)

# --- Radio Buttons ---
# Create a variable to store the selected radio button's value.
radio_var = tk.StringVar(value="option1")  # Default selection

radio1 = tk.Radiobutton(frame, text="Option 1", variable=radio_var, value="option1")
radio1.pack(pady=5)

radio2 = tk.Radiobutton(frame, text="Option 2", variable=radio_var, value="option2")
radio2.pack(pady=5)


# Create the menu bar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Open menu
open_menu = Menu(menubar, tearoff=0)
open_menu.add_command(label="Open Text", command=open_text)
open_menu.add_separator()
open_menu.add_command(label="Open CSV", command=open_csv)
open_menu.add_separator()
open_menu.add_command(label="Open XML", command=open_xml)
open_menu.add_separator()
open_menu.add_command(label="Open JSON", command=open_json)
open_menu.add_separator()
open_menu.add_command(label="Open Binary", command=open_binary)
open_menu.add_separator()
open_menu.add_command(label="Open Object", command=open_object)
menubar.add_cascade(label="Open", menu=open_menu)

# Save menu
save_menu = Menu(menubar, tearoff=0)
save_menu.add_command(label="Save Text", command=save_text)
save_menu.add_separator()
save_menu.add_command(label="Save CSV", command=save_csv)
save_menu.add_separator()
save_menu.add_command(label="Save XML", command=save_xml)
save_menu.add_separator()
save_menu.add_command(label="Save JSON", command=save_json)
save_menu.add_separator()
save_menu.add_command(label="Save Binary", command=save_binary)
save_menu.add_separator()
save_menu.add_command(label="Save Object", command=save_object)
menubar.add_cascade(label="Save", menu=save_menu)

# Run the application
root.mainloop()

# -- end --