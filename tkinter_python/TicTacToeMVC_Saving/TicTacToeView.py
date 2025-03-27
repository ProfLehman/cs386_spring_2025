import tkinter as tk

class TicTacToeView:
    
    def __init__(self, controller):
        
        # save link back to controller
        self.controller = controller
        
        # setup window for Tic Tac Toe GUI Board using buttons
        self.main = tk.Tk()
        self.main.title("Tic Tac Toe")
        self.main.geometry("400x500")
        
        self.main_frame = tk.Frame(self.main)
        self.main_frame.pack()

        self.status_frame = tk.Frame(self.main_frame)
        self.status_frame.grid(row=0, column=0, columnspan=3)
        self.status_label = tk.Label(self.status_frame, text="Player X's turn", font=("Arial", 18))
        self.status_label.pack(pady=10)

        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.grid(row=1, column=0, columnspan=3)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.grid_frame, text="", font=("Arial", 20), width=5, height=2,
                                               command=lambda r=i, c=j: self.handle_selection(r, c))
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_frame = tk.Frame(self.main_frame)
        self.reset_frame.grid(row=2, column=0, columnspan=3)
        
        self.reset_button = tk.Button(self.reset_frame, text="Reset", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        self.save_button = tk.Button(self.reset_frame, text="Save", font=("Arial", 14), command=self.save_game)
        self.save_button.pack(pady=10)
        
        self.open_button = tk.Button(self.reset_frame, text="Open", font=("Arial", 14), command=self.open_game)
        self.open_button.pack(pady=10)
        
        
    # tell controller to handle selection
    def handle_selection(self, row, col):
        print( "Handle Selection", row, col )
        self.controller.handle_selection(row, col)
        
    # update board with value
    def update_board(self, row, col, value):
        self.buttons[row][col].config(text=str(value))
    
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
        
    # tell controller to save game with filename
    def save_game(self):
        #self.controller.save_game("game.txt")
        self.controller.save_game("game.obj")
     
    def open_game(self):
        #self.controller.open_game("game.txt")
        self.controller.open_game("game.obj")
        
if __name__ == "__main__":
    test = TicTacToeView( None )
 
    