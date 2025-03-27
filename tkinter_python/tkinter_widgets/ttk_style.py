#  ttk_style.py
# spring 2025
# prof. lehman
# ChatCPT 4o summaory of ttk style options

# The ttk.Style().configure() method allows you to customize the appearance of ttk widgets. 

# General Options (Applicable to Most Widgets)

#        font: Sets the font type, size, and style.
#     Example: font=("Arial", 12, "bold")

#  foreground: Sets the text (or foreground) color.
#     Example: foreground="blue"

#  background: Sets the widget’s background color (note: limited support, requires platform compatibility or themes).
#     Example: background="lightgray"

#     padding: Adds padding inside the widget (around the content).
#     Example: padding=10 or padding=(5, 10)

#      relief: Specifies the border style (flat, raised, sunken, solid, etc.).
#     Example: relief="flat"

# borderwidth: Specifies the width of the widget border.
#     Example: borderwidth=2


import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("All ttk Widgets Example")

# ttk Style configuration
style = ttk.Style()
style.configure("Custom.TLabel", font=("Arial", 16, "italic"), foreground="red", background="black")
style.configure("Custom.TEntry", foreground="orange", background="blue", font=("Arial", 18, "bold"))
style.configure("Custom.TButton", font=("Arial", 16, "bold"), padding=10, foreground="blue", background="green")

# Three ttk.Label widgets with one styled
ttk.Label(root, text="Regular Label 1").grid(row=0, column=0, padx=10, pady=5)
ttk.Label(root, text="Regular Label 2").grid(row=0, column=1, padx=10, pady=5)
ttk.Label(root, text="Styled Label", style="Custom.TLabel").grid(row=0, column=2, padx=10, pady=5)

# Three ttk.Entry widgets with one styled
ttk.Entry(root).grid(row=1, column=0, padx=10, pady=5)
ttk.Entry(root).grid(row=1, column=1, padx=10, pady=5)
ttk.Entry(root, style="Custom.TEntry").grid(row=1, column=2, padx=10, pady=5)  # Styled with green text


# Note: The font option in ttk.Style does not directly affect the text size in ttk.Entry widgets. 
# This is because the ttk.Entry widget relies on the underlying native widget provided by the 
# operating system, which may not support font changes through the style.
# To fix this, you can set the font directly on the ttk.Entry widget itself, as follows:
# ttk.Entry(root, style="Custom.TEntry", font=("Comic Sans MS", 18, "bold")).grid(row=1, column=2, padx=10, pady=5)  # Styled with green text

# Three ttk.Button widgets with one styled
ttk.Button(root, text="Button 2").grid(row=2, column=0, padx=10, pady=5)
ttk.Button(root, text="Button 1").grid(row=2, column=1, padx=10, pady=5)
ttk.Button(root, text="Styled Button", style="Custom.TButton").grid(row=2, column=2, padx=10, pady=5)  # Styled button

root.mainloop()


