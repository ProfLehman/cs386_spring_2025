# -----------------------------------------------
#     Program: basics_menus_about_image.py
#
#      Author: Prof. Lehman
#
#        Date: 17 January 2025
#
# Description: demonstrates about window with image
#              and menus
# -----------------------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Button

from PIL import Image, ImageTk

import os

def show_about():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("250x500")
    about_window.resizable(False, False) # horizontal and vertical

    # Load and display the image using Pillow with an absolute path
    try:
        image = Image.open("me.png")
        photo = ImageTk.PhotoImage(image)
        img_label = Label(about_window, image=photo)
        img_label.image = photo  # Keep a reference
        img_label.grid(row=0, column=1, padx=(22, 10), pady=5)
    except Exception as e:
        messagebox.showerror("File Exception with me.jpg")

    # Display the creation date
    title_label = Label(about_window, text="My App")
    title_label.grid(row=1, column=1, padx=10, pady=10)
    
    author_label = Label(about_window, text="Prof. Lehman")
    author_label.grid(row=2, column=1, padx=10, pady=5)

    version_label = Label(about_window, text="Version 1.0")
    version_label.grid(row=3, column=1, padx=10, pady=5)

    date_label = Label(about_window, text="17 January 2025")
    date_label.grid(row=4, column=1, padx=10, pady=5)

    ok_button = Button(about_window, text="OK", command=about_window.destroy)  
    ok_button.grid(row=5, column=1, padx=10, pady=(10,50))
    
    
# Initialize the main window
root = tk.Tk()
root.title("Basics - about window, image, menus")
root.geometry("400x200")

# Menu
menu_bar = tk.Menu(root) #create menu bar

# Setup File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command="")
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=root.destroy)

# Steup Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)

# add menus to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar) #add menu bar to window

# Start the main loop
root.mainloop()

