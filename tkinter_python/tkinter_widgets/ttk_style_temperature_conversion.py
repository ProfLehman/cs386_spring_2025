
# ttk_style_temperature_conversion.py
#
# prof. lehman
# spring 2025
#
# Generated with DeepSeek
#
# Prompts
#    1. Write a tkinter basic GUI with a label, textbox, and button to convert Fahrenheit to celsius.
#    2. Please update code to use ttk widgets.  Style the frame to be yellow.
#       The text input box should be green.  Make the answer bold.  Add a menu with File, clear, and exit.
#    3. What property tells the frame to expand left and right?
#
# Manual Adjustments
#    - changed padding for frame
#    - adjusted frame to fill space
#    - adjusted geometery
#    - fixed exit command to be root.destroy()


import tkinter as tk
from tkinter import ttk, messagebox, Menu

def convert_fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{celsius:.2f} °C", foreground="blue")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    #root.quit()
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Fahrenheit to Celsius Converter")
root.geometry("400x180")

# Style the frame with a yellow background
style = ttk.Style()
style.configure("Yellow.TFrame", background="yellow")

# Create a frame to hold the widgets
frame = ttk.Frame(root, style="Yellow.TFrame")
frame.pack(padx=5, pady=5, fill=tk.X)

# Create a label for instructions
instruction_label = ttk.Label(frame, text="Enter temperature in Fahrenheit:", background="yellow")
instruction_label.pack(pady=10)

# Create an entry widget for user input with a green background
entry = ttk.Entry(frame, style="Green.TEntry")
style.configure("Green.TEntry", fieldbackground="green")
entry.pack(pady=10)

# Create a button to trigger the conversion
convert_button = ttk.Button(frame, text="Convert", command=convert_fahrenheit_to_celsius)
convert_button.pack(pady=10)

# Create a label to display the result in bold
result_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"), background="yellow")
result_label.pack(pady=10)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear", command=clear_fields)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Start the Tkinter event loop
root.mainloop()
