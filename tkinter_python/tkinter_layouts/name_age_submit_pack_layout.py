import tkinter as tk

root = tk.Tk()
root.title("Pack Layout")
root.geometry("250x100")

# Frame for the name input
name_frame = tk.Frame(root)
name_frame.pack(fill='x', padx=10, pady=5)

# Label for name inside the frame
name_label = tk.Label(name_frame, text="Name:")
name_label.pack(side='left')

# Entry widget for name
name_entry = tk.Entry(name_frame)
name_entry.pack(side='left', fill='x', expand=True)

# Frame for the age input
age_frame = tk.Frame(root)
age_frame.pack(fill='x', padx=10, pady=5)

# Label for age inside the frame
age_label = tk.Label(age_frame, text="Age:")
age_label.pack(side='left')

# Entry widget for age
age_entry = tk.Entry(age_frame)
age_entry.pack(side='left', fill='x', expand=True)

# Frame for the submit button
submit_frame = tk.Frame(root)
submit_frame.pack(fill='x', padx=10, pady=5)

# Submit button
submit_button = tk.Button(submit_frame, text="Submit")
submit_button.pack(fill='x')

root.mainloop()
