# tk_vs_ttk.py
# spring 2025
# prof. lehman
# ChatCPT 4o summaory of tk vs ttk widgets
#

# The ttk module in Tkinter provides themed versions of many commonly used widgets. 
# These ttk widgets are designed to have a more modern look and feel and adapt to the 
# native appearance of the operating system. Here's a list of the widgets available in ttk:

# Widgets with ttk Options
# Container Widgets:

# ttk.Frame: A container to hold other widgets, with themed styling options.
# ttk.LabelFrame: A container widget with a label (like Frame but includes a title).

# Input Widgets:

# ttk.Button: A styled button.
# ttk.Checkbutton: A checkbox that supports styling.
# ttk.Radiobutton: A styled radio button.
# ttk.Entry: A single-line text entry field.
# ttk.Combobox: A drop-down list with editable or non-editable options.
# ttk.Spinbox: An entry widget with increment/decrement arrows.
# ttk.Scale: A slider for selecting a numeric value.


# Display Widgets:

# ttk.Label: A styled text or image display label.
# ttk.Progressbar: A bar to show progress (indeterminate or determinate).

#  Selection Widgets:

# ttk.Notebook: A tabbed container for organizing content into pages.
# ttk.Treeview: A widget for displaying hierarchical data in a tree-like format.
# ttk.Listbox: A styled list widget (though not as commonly themed as others).

# Layout Widgets:
# ttk.PanedWindow: A container to organize resizable panes.

# Other Widgets:

#  ttk.Separator: A horizontal or vertical line separator.
# ttk.Menubutton: A button that opens a menu.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("tk vs ttk Widgets Demo")

  
# tk and ttk Labels
tk.Label(root, text="tk.Label", bg="lightgray").grid(row=0, column=0, padx=10, pady=5)
ttk.Label(root, text="ttk.Label").grid(row=0, column=1, padx=10, pady=5)

# tk and ttk Entry
tk.Entry(root).grid(row=1, column=0, padx=10, pady=5)
ttk.Entry(root).grid(row=1, column=1, padx=10, pady=5)

# tk and ttk Button
tk.Button(root, text="tk.Button").grid(row=2, column=0, padx=10, pady=5)
ttk.Button(root, text="ttk.Button").grid(row=2, column=1, padx=10, pady=5)

# tk and ttk Checkbutton
tk.Checkbutton(root, text="tk.Checkbutton").grid(row=3, column=0, padx=10, pady=5)
ttk.Checkbutton(root, text="ttk.Checkbutton").grid(row=3, column=1, padx=10, pady=5)

# tk and ttk Radiobutton
tk.Radiobutton(root, text="tk.Radiobutton").grid(row=4, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="ttk.Radiobutton").grid(row=4, column=1, padx=10, pady=5)

# tk and ttk Scale
tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL).grid(row=5, column=0, padx=10, pady=5)
ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL).grid(row=5, column=1, padx=10, pady=5)

# tk and ttk Combobox (only ttk has it, tk uses OptionMenu)
options = ["Option 1", "Option 2", "Option 3"]
tk.OptionMenu(root, tk.StringVar(value=options[0]), *options).grid(row=6, column=0, padx=10, pady=5)
ttk.Combobox(root, values=options).grid(row=6, column=1, padx=10, pady=5)

# tk and ttk Progressbar (only ttk has it)
ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode="determinate", value=50).grid(row=7, column=1, padx=10, pady=5)
tk.Label(root, text="tk lacks Progressbar").grid(row=7, column=0, padx=10, pady=5)

root.mainloop()






