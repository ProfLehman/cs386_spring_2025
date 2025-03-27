import tkinter as tk

# buttonClicks.py

def on_button_click(row, col):
    print(f"Button at ({row}, {col}) clicked")
    buttons[row][col].config(text="Clicked")

# Create main application window
root = tk.Tk()
root.title("3x3 Grid Button Clicks")

# Create a 3x3 grid of buttons
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=f"({i},{j})", width=10, height=3,
                           command=lambda r=i, c=j: on_button_click(r, c))
        button.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Run the Tkinter event loop
root.mainloop()