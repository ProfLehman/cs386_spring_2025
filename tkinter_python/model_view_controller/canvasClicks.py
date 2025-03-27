import tkinter as tk

# canvasClicks.py

# Alternative Mouse Events:
# <Button-2> → Middle mouse button
# <Button-3> → Right mouse button
# <Double-Button-1> → Double-click with the left mouse button
# <ButtonRelease-1> → Detects when the left mouse button is released
# <Motion> → Detects mouse movement


# Constants
BOARD_SIZE = 300  # Size of the canvas
CELL_SIZE = BOARD_SIZE // 3  # Size of each cell

def draw_board(canvas):
    """Draws the Tic-Tac-Toe grid."""
    for i in range(1, 3):
        # Vertical lines
        canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, BOARD_SIZE, width=2)
        # Horizontal lines
        canvas.create_line(0, i * CELL_SIZE, BOARD_SIZE, i * CELL_SIZE, width=2)

def get_cell(event):
    """Handles mouse clicks and determines the clicked cell."""
    row = event.y // CELL_SIZE
    col = event.x // CELL_SIZE
    print(f"Clicked cell: ({row}, {col})")  # This can be used to place Xs and Os later

# Create main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create canvas
canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE, bg="white")
canvas.pack()

# Draw the Tic-Tac-Toe grid
draw_board(canvas)

# Bind click event to the canvas
canvas.bind("<Button-1>", get_cell)

# Run the Tkinter event loop
root.mainloop()
