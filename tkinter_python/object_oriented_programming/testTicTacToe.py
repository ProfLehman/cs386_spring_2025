
from TicTacToe import *

# game is an instance of TicTacToe
game = TicTacToe("Chidi", "Clay")

game.display_players()
game.display_game()

row = int( input("Enter row: ") )
col = int( input("Enter col: ") )

game.play_xo( game.get_turn(), row, col)
game.display_game()

game.play_xo(game.get_turn(), 1, 1)
game.display_game()

