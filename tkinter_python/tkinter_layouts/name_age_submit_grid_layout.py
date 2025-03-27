import tkinter as tk

root = tk.Tk()
root.title("Grid Layout")
root.geometry("250x100")

# Label for name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky='E', padx=10, pady=5)

# Entry widget for name
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, columnspan=2, sticky='WE', padx=10, pady=5)

# Label for age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, sticky='E', padx=10, pady=5)

# Entry widget for age
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, sticky='WE', padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=2, column=0, columnspan=3, sticky='EW', padx=10, pady=5)

root.mainloop()