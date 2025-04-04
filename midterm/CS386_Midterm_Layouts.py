import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")

        self.selected_cell = None
        self.board = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        # Sudoku Grid
        grid_frame = tk.Frame(self.root)
        grid_frame.grid(row=0, column=1, padx=10, pady=10)

        for row in range(9):
            for col in range(9):
                cell = tk.Entry(grid_frame, width=2, font=('Arial', 18), justify='center', bd=1, relief='solid')
                cell.grid(row=row, column=col, padx=1, pady=1)
                cell.bind("<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))
                self.board[row][col] = cell

        # Number Pad
        pad_frame = tk.Frame(self.root)
        pad_frame.grid(row=0, column=0, padx=10, pady=10)

        buttons = [
            '1', '2', '3', '4',
            '5', '6', '7', '8',
            '9', 'X'
        ]
        for i, label in enumerate(buttons):
            button = tk.Button(pad_frame, text=label, width=4, height=2, font=('Arial', 14),
                               command=lambda l=label: self.on_number_click(l))
            # this greats a x5 row by x2 columns
            button.grid(row=i//2, column=i%2, padx=2, pady=2)

        # Hint Button
        hint_button = tk.Button(self.root, text="HINT", width=20, height=2, font=('Arial', 14), command=self.give_hint)
        hint_button.grid(row=1, column=1, pady=10)

    def select_cell(self, row, col):
        self.selected_cell = (row, col)

    def on_number_click(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if value == 'X':
                self.board[row][col].delete(0, tk.END)
            else:
                self.board[row][col].delete(0, tk.END)
                self.board[row][col].insert(0, value)

    def give_hint(self):
        messagebox.showinfo("Hint", "Hint functionality not implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
