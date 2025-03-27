
# dice_roller10.py
# spring 2025
# prof. lehman
#
# dice roller for Qwixx game
# developed by series of approximately 10 ChatGPT 4o prompts
# including a sketch of the desired GUI
#
# light blue color code added manually
#

import tkinter as tk
import random

def roll_all():
    """Roll all dice."""
    for color, var in dice_variables.items():
        var.set(random.randint(1, 6))
    update_totals()

def update_totals():
    """Update the totals for all combinations."""
    white1 = dice_variables["White 1"].get()
    white2 = dice_variables["White 2"].get()
    everyone_var.set(white1 + white2)

    red_var1.set(dice_variables["Red"].get() + white1)
    red_var2.set(dice_variables["Red"].get() + white2)

    yellow_var1.set(dice_variables["Yellow"].get() + white1)
    yellow_var2.set(dice_variables["Yellow"].get() + white2)

    green_var1.set(dice_variables["Green"].get() + white1)
    green_var2.set(dice_variables["Green"].get() + white2)

    blue_var1.set(dice_variables["Blue"].get() + white1)
    blue_var2.set(dice_variables["Blue"].get() + white2)

# Initialize the main window
root = tk.Tk()
root.title("Qwixx Dice Roller")

# Dice colors
dice_colors = ["White 1", "White 2", "Red", "Yellow", "Green", "Blue"]

# Variables for dice values
dice_variables = {color: tk.IntVar(value=1) for color in dice_colors}

# Create a frame for the dice
frame = tk.Frame(root)
frame.pack(pady=10)

# Display dice with labels horizontally
for i, color in enumerate(dice_colors):
    tk.Label(frame, text=color).grid(row=0, column=i, padx=10, pady=5)
    if color == "Blue":
        tk.Label(frame, textvariable=dice_variables[color], font=("Helvetica", 24), width=2, relief="solid", bg="light blue").grid(row=1, column=i, padx=10, pady=5)
    else:
        tk.Label(frame, textvariable=dice_variables[color], font=("Helvetica", 24), width=2, relief="solid", bg="white" if "White" in color else color.lower()).grid(row=1, column=i, padx=10, pady=5)

# Create a frame for totals
totals_frame = tk.Frame(root)
totals_frame.pack(pady=10)

# Add labels for totals
tk.Label(totals_frame, text="Everyone").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
tk.Label(totals_frame, text="Player Red").grid(row=0, column=2, columnspan=2, padx=10, pady=5)
tk.Label(totals_frame, text="Yellow").grid(row=0, column=4, columnspan=2, padx=10, pady=5)
tk.Label(totals_frame, text="Green").grid(row=0, column=6, columnspan=2, padx=10, pady=5)
tk.Label(totals_frame, text="Blue").grid(row=0, column=8, columnspan=2, padx=10, pady=5)

# Add totals below the dice
everyone_var = tk.IntVar(value=0)
temp = tk.Entry(totals_frame, textvariable=everyone_var, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="white")
temp.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

red_var1 = tk.IntVar(value=0)
red_var2 = tk.IntVar(value=0)
tk.Entry(totals_frame, textvariable=red_var1, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="red").grid(row=1, column=2, padx=5)
tk.Entry(totals_frame, textvariable=red_var2, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="red").grid(row=1, column=3, padx=5)

yellow_var1 = tk.IntVar(value=0)
yellow_var2 = tk.IntVar(value=0)
tk.Entry(totals_frame, textvariable=yellow_var1, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="yellow").grid(row=1, column=4, padx=5)
tk.Entry(totals_frame, textvariable=yellow_var2, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="yellow").grid(row=1, column=5, padx=5)

green_var1 = tk.IntVar(value=0)
green_var2 = tk.IntVar(value=0)
tk.Entry(totals_frame, textvariable=green_var1, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="green").grid(row=1, column=6, padx=5)
tk.Entry(totals_frame, textvariable=green_var2, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="green").grid(row=1, column=7, padx=5)

blue_var1 = tk.IntVar(value=0)
blue_var2 = tk.IntVar(value=0)
tk.Entry(totals_frame, textvariable=blue_var1, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="light blue").grid(row=1, column=8, padx=5)
tk.Entry(totals_frame, textvariable=blue_var2, font=("Helvetica", 18), width=5, justify="center", state="readonly", readonlybackground="light blue").grid(row=1, column=9, padx=5)

# Button to roll all dice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

roll_all_button = tk.Button(button_frame, text="Roll", command=roll_all)
roll_all_button.pack()

# Initialize totals
update_totals()

# Run the application
root.mainloop()
