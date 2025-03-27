import tkinter as tk

BOARD_SIZE = 300  # Size of the canvas
CELL_SIZE = BOARD_SIZE // 3  # Size of each cell
    
class TicTacToeView_Canvas:
        
    def __init__(self, controller):

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
        #self.buttons[row][col].config(text=str(value))
        print( "update board" )
        
        if value == "X":
            self.drawX( row, col )
        elif value == "O":
            self.drawO( row, col )
        else:
            self.canvas.delete("xo")
            
            
    # drawX
    def drawX( self, r, c ):  
        
        s = CELL_SIZE            # width and height ie. size of cell
        sp = 15                  # spacing around edge
        es = CELL_SIZE - (2*sp)  # effective size of X or 0
        
        # top left to bottom right
        over = (c * s) + sp
        down = (r * s) + sp
        self.canvas.create_line(over, down, over+es, down+es, fill="blue", width=3, tags="xo")
        
        # bottom left to top right
        self.canvas.create_line(over, down+es, over+es, down, fill="blue", width=3, tags="xo")
        
    #drawO
    def drawO( self, r, c):
        s = CELL_SIZE            # width and height ie. size of cell
        sp = 15                  # spacing around edge
        es = CELL_SIZE - (2*sp)  # effective size of X or 0
        
        over = (c * s) + sp
        down = (r * s) + sp
        self.canvas.create_oval(over, down, over+es, down+es, outline="red", width=3, tags="xo")
    
    
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
        

 
    
