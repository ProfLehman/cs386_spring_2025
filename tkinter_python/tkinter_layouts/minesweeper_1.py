# minesweeper_1.py
# prof. lehman
# spring 2025
#
# sample GUI created from screenshot of minesweeper
#
# Used ChatGPT 4o prompts (x2)
# 1. Create a tkinter GUI non functional from attached image.
# 2. Update gui to include a slider at bottom.
#
# manually adjusted geometry, modified padding, removed label that was orignally shown for slider
# removed UTF smiley face and used ":-)"

import tkinter as tk
from tkinter import ttk

def create_gui():
    root = tk.Tk()
    root.title("Minesweeper")

    # Configure grid
    root.geometry("250x350")

    # Top panel
    top_frame = tk.Frame(root, bg="gray", height=50)
    top_frame.pack(fill=tk.X)

    # Digital displays and face button
    left_display = tk.Label(top_frame, text="000", bg="black", fg="red", font=("Courier", 20), width=3, height=1)
    left_display.pack(side=tk.LEFT, padx=20)

    face_button = tk.Button(top_frame, text=":-)", bg="yellow", font=("Arial", 12), width=3, height=1)
    face_button.pack(side=tk.LEFT, padx=20)

    right_display = tk.Label(top_frame, text="000", bg="black", fg="red", font=("Courier", 20), width=3, height=1)
    right_display.pack(side=tk.LEFT, padx=10)

    # Game grid
    grid_frame = tk.Frame(root, bg="white")
    grid_frame.pack(pady=5)

    # Create grid buttons (9x9 example)
    for row in range(9):
        for col in range(9):
            cell = tk.Button(grid_frame, text="", width=2, height=1, relief=tk.RAISED, bg="lightgray")
            cell.grid(row=row, column=col, padx=1, pady=1)

    # Bottom panel
    bottom_frame = tk.Frame(root)
    bottom_frame.pack()

    # Slider at bottom
    slider = tk.Scale(bottom_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
    slider.pack(pady=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
