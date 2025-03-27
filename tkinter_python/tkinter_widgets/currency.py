# currency.py
# spring 2025
# prof. lehman
#
# currency converter
#
# code developed from ChatGPT 4o prompts
#
# note: had to install Pillow package for images
#

import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Button
from datetime import datetime
from PIL import Image, ImageTk
import os


def convert_currency():
    try:
        amount = float(amount_entry.get())
        
        if conversion_direction.get() == "USD to CAD":
            result = amount * usd_to_cad_rate
            result_label.config(text=f"${amount} USD = ${result:.2f} CAD")
        
        else:
            result = amount * cad_to_usd_rate
            result_label.config(text=f"${amount} CAD = ${result:.2f} USD")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def clear_data():
    amount_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here.")

def update_usd_to_cad_rate():
    global usd_to_cad_rate, cad_to_usd_rate
    try:
        new_rate = simpledialog.askfloat("Update USD to CAD Rate", "Enter new USD to CAD rate:")
        if new_rate and new_rate > 0:
            usd_to_cad_rate = new_rate
            cad_to_usd_rate = 1 / new_rate
            messagebox.showinfo("Success", f"USD to CAD rate updated to {usd_to_cad_rate}\nCAD to USD rate updated to {cad_to_usd_rate:.4f}")
        else:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
usd_to_cad_rate = 1.43588
cad_to_usd_rate = 1 / usd_to_cad_rate
def update_cad_to_usd_rate():
    global usd_to_cad_rate, cad_to_usd_rate
    try:
        new_rate = simpledialog.askfloat("Update CAD to USD Rate", "Enter new CAD to USD rate:")
        if new_rate and new_rate > 0:
            cad_to_usd_rate = new_rate
            usd_to_cad_rate = 1 / new_rate
            messagebox.showinfo("Success", f"CAD to USD rate updated to {cad_to_usd_rate}\nUSD to CAD rate updated to {usd_to_cad_rate:.4f}")
        else:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def show_about():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x450")

    # Load and display the image using Pillow with absolute path
    try:
        image = Image.open("me.png")
        photo = ImageTk.PhotoImage(image)
        img_label = Label(about_window, image=photo)
        img_label.image = photo  # Keep a reference
        img_label.pack(pady=10)
    except Exception as e:
        Label(about_window, text=f"Image not found. {e}").pack(pady=10)

    # Display the creation date
    Label(about_window, text="USA to Canadian Currency Converter").pack(pady=5)
    Label(about_window, text="Prof. Lehman").pack(pady=5)
    Label(about_window, text="Version 1.0").pack(pady=5)
    Label(about_window, text="15 January 2025").pack(pady=5)

    # Pass the about_window to the close_window function
    Button(about_window, text="OK", command=lambda: close_window(about_window)).pack(pady=5)

def close_window(window):
    window.destroy()
    
# Initialize the main window
root = tk.Tk()
root.title("USD <-> CAD Currency Converter")
root.geometry("400x200")

# Conversion rates
usd_to_cad_rate = 1.43588
cad_to_usd_rate = 1 / usd_to_cad_rate

msg=f"US to CAN {usd_to_cad_rate}, \nCAN to US {cad_to_usd_rate}"

#messagebox.showinfo(message=msg, title="Current Rates")

# Input field
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

amount_entry = tk.Entry(root, width=30)
amount_entry.insert(0,"100")
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Radio buttons for conversion direction
conversion_direction = tk.StringVar(value="USD to CAD")
usd_to_cad_radio = tk.Radiobutton(root, text="USD to CAD", variable=conversion_direction, value="USD to CAD")
usd_to_cad_radio.grid(row=1, column=0, padx=10, pady=5, sticky='w')

cad_to_usd_radio = tk.Radiobutton(root, text="CAD to USD", variable=conversion_direction, value="CAD to USD")
cad_to_usd_radio.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result will appear here.")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Menu
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

# Rates Menu
rates_menu = tk.Menu(menu_bar, tearoff=0)
rates_menu.add_command(label="Update USD to CAD Rate", command=update_usd_to_cad_rate)
rates_menu.add_command(label="Update CAD to USD Rate", command=update_cad_to_usd_rate)
menu_bar.add_cascade(label="Rates", menu=rates_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

#msg=f"US to CAN {usd_to_cad_rate}, \nCAN to US {cad_to_usd_rate}"
#messagebox.showinfo(message=msg, title="Current Rates")

# Start the main loop
root.mainloop()

