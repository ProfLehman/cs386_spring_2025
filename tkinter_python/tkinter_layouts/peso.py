# peso.py
# prof. lehman
# spring 2025
#
# sample GUI created from GUI sketch on chalkboard
#
# Used ChatGPT 4o prompts (x2)
# 1. Create a working Peso to US dollar currency converter.  Assume exchange rate is 4,000 pesos to 1 us dollar.  
#    Format amounts to two decimal places.  Add a clear menu and a exit menu.
# 2. Looks good, except move button to right as shown in sample sketch.
#
# note: manually adjusted button to right location after AI prompt failed
#       adjusted geometry
#

import tkinter as tk
from tkinter import ttk

def create_converter():
    def convert():
        try:
            pesos = float(entry_peso.get())
            dollars = pesos / 4000
            entry_dollar.delete(0, tk.END)
            entry_dollar.insert(0, f"{dollars:.2f}")
        except ValueError:
            entry_dollar.delete(0, tk.END)
            entry_dollar.insert(0, "Error")

    def clear():
        entry_peso.delete(0, tk.END)
        entry_dollar.delete(0, tk.END)

    def exit_app():
        root.destroy()

    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("350x180")
    
    # Menu
    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Clear", command=clear)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)

    # Title label
    title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Peso input
    label_peso = tk.Label(root, text="Peso:", font=("Arial", 12))
    label_peso.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_peso = tk.Entry(root, font=("Arial", 12), width=15)
    entry_peso.grid(row=1, column=1, padx=10, pady=5)

    # Dollar output
    label_dollar = tk.Label(root, text="US Dollars:", font=("Arial", 12))
    label_dollar.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_dollar = tk.Entry(root, font=("Arial", 12), width=15)
    entry_dollar.grid(row=2, column=1, padx=10, pady=5)

    # Convert button
    convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert)
    convert_button.grid(row=1, column=2, rowspan=2, pady=10, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    create_converter()
