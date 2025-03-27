import tkinter as tk

# TicTacToeView_Canvas.py
# spring 2025
# prof. lehman
# CS382 Visual Programming P4
# demonstrates MVC architecture
# model, view, controller

# GUI using canvas
#
# ** to do ** fix graphics to display X and O that fits into space
#             update colors for X and O
#             fix reset to draw a new board
#

BOARD_SIZE = 300  # Size of the canvas
CELL_SIZE = BOARD_SIZE // 3  # Size of each cell
    
class TicTacToeView_Canvas:
        
    def __init__(self, controller):

        # Constants


        # save link back to controller
        self.controller = controller
        
        # setup window for Tic Tac Toe GUI Board using buttons
        # Setup window
        self.main = tk.Tk()
        self.main.title("Tic Tac Toe")
        self.main.geometry("400x600")

        # Main frame
        self.main_frame = tk.Frame(self.main)
        self.main_frame.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.main_frame, text="Player X's turn", font=("Arial", 18))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Canvas for Tic Tac Toe board
        self.canvas = tk.Canvas(self.main_frame, width=BOARD_SIZE, height=BOARD_SIZE, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3, pady=10)

        # Draw Tic-Tac-Toe grid
        for i in range(1, 3):
            # Vertical lines
            self.canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, BOARD_SIZE, width=2)
            # Horizontal lines
            self.canvas.create_line(0, i * CELL_SIZE, BOARD_SIZE, i * CELL_SIZE, width=2)

        # Bind click event
        self.canvas.bind("<Button-1>", self.handle_selection)

        # Reset button
        self.reset_button = tk.Button(self.main_frame, text="Reset", font=("Arial", 14), command=self.reset_game)
        self.reset_button.grid(row=2, column=0, columnspan=3, pady=10)    
    
    # tell controller to handle selection
    def handle_selection(self, event):
        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        
        print( "Handle Selection", row, col )
        self.controller.handle_selection(row, col)
        
    # update board with value
    def update_board(self, row, col, value):
        print( "update board" )
        
        if value == "X":
            self.drawX( row, col )
        elif value == "O":
            self.drawO( row, col )
        else:
            self.canvas.delete("all")
            
    # drawX
    def drawX( self, r, c ):  
        print( r, c )
        over = c * CELL_SIZE
        down = (r * CELL_SIZE) + 10
        self.canvas.create_line(over, down, over+CELL_SIZE-10, down+CELL_SIZE-10, width=2)
        
    #drawO
    def drawO( self, r, c):
        over = c * CELL_SIZE
        down = (r * CELL_SIZE) + 10
        self.canvas.create_oval(over, down, over+50, down+50, outline="black", width=2)
    
    # update status with msg
    def update_status(self, msg):
        self.status_label.config(text=f"{msg}")
           
    # tell controller to reset game
    def reset_game(self):
        self.controller.reset_game()
        
    # start loop and wait for clicks
    def run(self):
        print("view run")
        self.main.mainloop()
        
        
if __name__ == "__main__":
    test = TicTacToeView_Canvas( None )
 
    
