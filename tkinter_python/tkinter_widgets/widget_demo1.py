# widget_demo1.py
# prof. lehman
# 13 January 2025
# demonstrates basic tkInter widgets
#
# initial code outline created with ChatGPT 4o prompt
#    Create a simple tkInter form to introduce standard widgets.  
#    The form will include three radio buttons, a checkbox, a textbox, 
#    a label, a button, and a menu with file, clear, and exit.  
#    Display the status or data from each component in a message box 
#    when the button is pressed. Use a grid layout approach.
#
# modifications made to show_data to more clearly extract state of widgets
# and display data on form window

import tkinter as tk
from tkinter import messagebox

# Function to display data from widgets
def show_data():
    
    selected_radio = radio_var.get()
    checkbox_status = checkbox_var.get()
    textbox_content = textbox.get()
    
    message = (
        f"Selected Radio Button: {selected_radio}\n"
        f"Checkbox Status: {checkbox_status}\n"
        f"Textbox Content: {textbox_content}"
    )
    messagebox.showinfo("Form Data", message)

# Function to clear all fields
def clear_form():
    radio_var.set(None)
    checkbox_var.set(0)
    textbox.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Tkinter Widgets Demo")
root.geometry("300x300")

# Radio Buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3")
radio1.grid(row=0, column=0, sticky='w', padx=10, pady=2)
radio2.grid(row=1, column=0, sticky='w', padx=10, pady=2)
radio3.grid(row=2, column=0, sticky='w', padx=10, pady=2)

# Checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=checkbox_var)
checkbox.grid(row=3, column=0, sticky='w', padx=10, pady=2)

# Textbox with label
label = tk.Label(root, text="Enter text:")
label.grid(row=4, column=0, sticky='w', padx=10, pady=2)
textbox = tk.Entry(root)
textbox.grid(row=5, column=0, sticky='w', padx=10, pady=2)

# Button to show data
button = tk.Button(root, text="Show Data", command=show_data)
button.grid(row=6, column=0, pady=10)

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_form)
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
