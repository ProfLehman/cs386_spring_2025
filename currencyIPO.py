# currencyIPO.py
# spring 2025
# prof. lehman
#
# currency converter demonstrates basic
# tkInter components using IPO model
# 
#

import tkinter as tk
from tkinter import messagebox


# function called by convert button
def convert_currency():
    try:
        # get amount from text box
        amount = float(amount_entry.get())
        
        # check conversion type and convert
        if conversion_direction.get() == "USD to CAD":
            x = "USD"
            y = "CAD"
            result = amount * usd_to_cad_rate
        else:
            result = amount * cad_to_usd_rate
            x = "CAD"
            y = "USD"
            
        # set label for result
        result_label.config(text=f"${amount} {x} = ${result:.2f} {y}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# clear input aout output
def clear_data():
    amount_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here.")

# Fixed conversion rates
usd_to_cad_rate = 1.42
cad_to_usd_rate = 1 / usd_to_cad_rate

# Initialize the main window
root = tk.Tk()
root.title("USD <-> CAD Currency Converter")
root.geometry("400x200")

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

root.config(menu=menu_bar)

# Start the main loop
root.mainloop()
