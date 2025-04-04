import tkinter as tk
from tkinter import messagebox

def calculate_price():
    try:
        price = float(price_entry.get())
        
        discount = 0.0

        if discount_var.get() == 0:
            discount = 0.0
        elif discount_var.get() == 1:
            discount = 0.1
        else:
            discount = 0.2
        
        discounted_price = price * (1 - discount)
                
        if tax_var.get() == 1:
            discounted_price *= 1.07  # Applying 7% tax
        
        result_label.config(text=f"Final Price: ${discounted_price:.2f}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the price.")

def clear_selections():
    price_entry.delete(0, tk.END)
    discount_var.set(0)  # Set to No Discount
    #discount_var.set("No Discount")  # *** unchecks all?
    tax_var.set(False)  # Uncheck tax checkbox
    result_label.config(text="Final Price: ")

# Create the main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("300x300")
root.configure(padx=10, pady=10)

# Price Label and Entry
price_label = tk.Label(root, text="Enter Price ($):")
price_label.grid(row=0, column=0, columnspan=2, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Frame for Discount Options
discount_var = tk.IntVar(value=1)
discount_frame = tk.Frame(root)
discount_frame.grid(row=2, column=0, pady=5, sticky="w")

discount_none = tk.Radiobutton(discount_frame, text="No Discount", variable=discount_var, value=0)
discount_none.pack(anchor="w", pady=2)
discount_10 = tk.Radiobutton(discount_frame, text="10% Discount", variable=discount_var, value=1)
discount_10.pack(anchor="w", pady=2)
discount_20 = tk.Radiobutton(discount_frame, text="20% Discount", variable=discount_var, value=2)
discount_20.pack(anchor="w", pady=2)

# Check Box for Tax Application
tax_var = tk.BooleanVar()
tax_checkbox = tk.Checkbutton(root, text="Apply Tax (7%)", variable=tax_var)
tax_checkbox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

# Calculate Button
calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_price)
calculate_button.pack(side=tk.LEFT, padx=5)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear", command=clear_selections)
clear_button.pack(side=tk.LEFT, padx=5)

# Result Label
result_label = tk.Label(root, text="Final Price: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
