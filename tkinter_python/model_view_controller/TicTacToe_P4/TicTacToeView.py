import tkinter as tk

# TicTacToeView.py
# spring 2025
# prof. lehman
# CS382 Visual Programming P4
# demonstrates MVC architecture
# model, view, controller

# GUI using Buttons
#
# link to controller, see *** to do ***

class TicTacToeView:
    
    def __init__(self, controller):
        
        # save link back to controller
        self.controller = controller
        
        # setup window for Tic Tac Toe GUI Board using buttons
        self.main = tk.Tk()
        self.main.title("Tic Tac Toe")
        self.main.geometry("400x400")
        
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
    
    # tell controller to handle selection
    def handle_selection(self, row, col):
        print( "Handle Selection", row, col )
        # *** to do *** tell controller to handle selection
        
    # update board with value
    def update_board(self, row, col, value):
        print("update board")
        # *** to do *** update button text with value
    
    # update status with msg
    def update_status(self, msg):
        print("update status")
        # *** to do *** update status text with msage
           
    # tell controller to reset game
    def reset_game(self):
        print("reset game")
        # *** to do ***  tell controller to reset game
        
    # start loop and wait for clicks
    def run(self):
        print("view run")
        self.main.mainloop()        
        
if __name__ == "__main__":
    test = TicTacToeView( None )
 
    