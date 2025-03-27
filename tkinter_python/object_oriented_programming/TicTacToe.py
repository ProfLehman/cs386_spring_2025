
# TicTacToe.py
# prof. lehman
# 28 January 2025
#
# class to implement logic for Tic Tac Toe game
#
# Code coverted (DeepSeek AI) from Java class develoed by Jeff Lehman, 1.0 March 24, 2017
#

class TicTacToe:
    """
    Class to support game logic of TicTacToe. 
    """

    def __init__(self, p1="Player X", p2="Player O"):
        """
        Default constructor. Initializes players, board, turn, and winner.
        """
        self.player1 = p1
        self.player2 = p2
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 board
        self.turn = 'X'  # Current turn ('X' or 'O')
        self.winner = 'N'  # Winner ('X', 'O', or 'N' for no winner)

    def clear_board(self):
        """
        Set the board to all blanks.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def set_player1(self, name):
        """
        Set the name of player 1 (always 'X').
        """
        self.player1 = name

    def set_player2(self, name):
        """
        Set the name of player 2 (always 'O').
        """
        self.player2 = name

    def get_player1(self):
        """
        Get the name of player 1.
        """
        return self.player1

    def get_player2(self):
        """
        Get the name of player 2.
        """
        return self.player2

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

    def display_players(self):
        """
        Display the names of the players.
        """
        print(f"Player X = {self.player1}")
        print(f"Player O = {self.player2}")

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


# Example usage
if __name__ == "__main__":
    game = TicTacToe("Alice", "Bob")
    game.display_players()
    game.display_game()

    # Play some moves
    game.play_xo('X', 0, 0)
    game.play_xo('O', 1, 1)
    game.play_xo('X', 0, 1)
    game.play_xo('O', 2, 2)
    game.play_xo('X', 0, 2)

    game.display_game()
    if game.is_game_over():
        print(f"Game over! Winner: {game.get_winner()}")
        


