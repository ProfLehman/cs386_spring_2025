
# TicTacToeModel.py
# prof. lehman
# 28 January 2025
#
# class to implement logic for Tic Tac Toe game
#
# Code coverted (DeepSeek AI) from Java class develoed by Jeff Lehman, 1.0 March 24, 2017
#

class TicTacToeModel:
    """
    Class to support game logic of TicTacToe. 
    """

    def __init__(self):
        """
        Default constructor. Initializes players, board, turn, and winner.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 board
        self.turn = 'X'  # Current turn ('X' or 'O')
        self.winner = 'N'  # Winner ('X', 'O', or 'N' for no winner)

    def reset_game(self):
        """
        Set the board to all blanks, reset turn, set playerX start
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.winner = 'N'

    def get_turn(self):
        """
        Get the current turn ('X' or 'O').
        """
        return self.turn

    def get_winner(self):
        """
        Get the winner ('X', 'O', or 'N' for no winner).
        """
        return self.winner

    def get_board_value(self, r, c):
        """
        Get the value at a specific board position.
        Returns 'E' if the position is invalid.
        """
        if 0 <= r <= 2 and 0 <= c <= 2:
            return self.board[r][c]
        else:
            return 'E'  # 'E' denotes an error

    def play_xo(self, xo, r, c):
        """
        Play 'X' or 'O' at a specific row and column.
        """
        if r < 0 or r > 2 or c < 0 or c > 2:
            print(f"Error: {r}, {c} is an invalid board position. Use 0-2, 0-2.")
        else:
            if self.turn == xo:
                if self.board[r][c] == ' ':
                    self.board[r][c] = xo
                    self.turn = 'O' if self.turn == 'X' else 'X'  # Switch turns
                    self.is_game_over()
                else:
                    print("Error: Spot is already taken.")
            else:
                print(f"Error: Hey, not your turn {xo}.")

    def display_game(self):
        """
        Display the game board in ASCII format.
        """
        print()
        for r in range(3):
            for c in range(3):
                print(f" {self.board[r][c]} ", end="")
                if c == 0 or c == 1:
                    print("|", end="")
            print()
            if r == 0 or r == 1:
                print("---|---|---")

    def is_game_over(self):
        """
        Determine if the game is over (winner or tie).
        Returns True if the game is over, otherwise False.
        """
        over = False

        # Check rows, columns, and diagonals for a winner
        xpos = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
        ypos = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 2, 1, 0]

        for w in range(0, len(xpos) - 2, 3):
            if (self.board[xpos[w]][ypos[w]] == self.board[xpos[w + 1]][ypos[w + 1]] and
                    self.board[xpos[w + 1]][ypos[w + 1]] == self.board[xpos[w + 2]][ypos[w + 2]] and
                    self.board[xpos[w]][ypos[w]] != ' '):
                over = True
                self.winner = self.board[xpos[w]][ypos[w]]

        # Check for a tie (all positions filled)
        if not over:
            over = True  # Assume game is over
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] != 'X' and self.board[r][c] != 'O':
                        over = False  # Game is not over if there's an empty spot

        return over

    def save_game(self, filename):    
        print("in save game")
        
        file = open(filename, mode='w')
        
        #save winner and turn
        file.write( f"{self.winner}\n" )
        file.write( f"{self.turn}\n" )
      
        #save board data
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    file.write("B\n")
                else:
                    file.write(f"{self.board[r][c]}\n")
                
        file.close()
        print(filename, "saved")
        
    def open_game(self, filename):    
        print("in open game")
        
        file = open(filename, mode='r')
        
        #save winner and turn
        self.winner = file.readline().strip()
        self.turn = file.readline().strip()
      
        print( self.winner, self.turn )
        
        #save board data
        for r in range(3):
            for c in range(3):
                
                self.board[r][c] = file.readline().strip()
                if self.board[r][c] == "B":
                    self.board[r][c] = " "
                    
        file.close()
        print(filename, "opened")
        
        
# --- end ---
        


