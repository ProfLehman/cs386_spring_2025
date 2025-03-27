import tkinter as tk

root = tk.Tk()
root.title("Place Layout")
root.geometry("250x100")

# Label for name
name_label = tk.Label(root, text="Name:")
name_label.place(x=10, y=10, width=40, height=20)

# Entry widget for name
name_entry = tk.Entry(root)
name_entry.place(x=60, y=10, width=180, height=20)

# Label for age
age_label = tk.Label(root, text="Age:")
age_label.place(x=10, y=40, width=40, height=20)

# Entry widget for age
age_entry = tk.Entry(root)
age_entry.place(x=60, y=40, width=180, height=20)

# Submit button
submit_button = tk.Button(root, text="Submit")
submit_button.place(x=10, y=70, width=230, height=25)

root.mainloop()

