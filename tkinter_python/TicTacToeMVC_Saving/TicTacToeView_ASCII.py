import tkinter as tk

class TicTacToeView_ASCII:
    
    def __init__(self, controller):
        
        # save link back to controller
        self.controller = controller
            
        # board is list of list of text values [" "
        self.board = [ [" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]
        
    #Display the game board in ASCII format.
    def display(self):
        print()
        for r in range(3):
            for c in range(3):
                print(f" {self.board[r][c]} ", end="")
                if c == 0 or c == 1:
                    print("|", end="")
            print()
            if r == 0 or r == 1:
                print("---|---|---")
                      
    # tell controller to handle selection
    def handle_selection(self, row, col):
        print( "Handle Selection", row, col )
        self.controller.handle_selection(row, col)
        
    # update board with value
    def update_board(self, row, col, value):
        self.board[row][col] = value
    
    # update status with msg
    def update_status(self, msg):
        print( msg )
           
    # tell controller to reset game
    def reset_game(self):
        self.controller.reset_game()
        
    # start loop and wait for clicks
    def run(self):
        print("view run")
        self.display()
        while True:
            r = int(  input("Enter row (-1 reset): ") )
            if r == -1:
                self.reset_game()
            else:
                c = int(  input("Enter col: ") )
                self.handle_selection( r, c )
                
            self.display()
        
if __name__ == "__main__":
    test = TicTacToeView_ASCII( None )
 
    
