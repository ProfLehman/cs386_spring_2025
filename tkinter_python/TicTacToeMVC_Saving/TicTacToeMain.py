
# TicTacToeMain.py
# 
# Spring 2025
#
# Prof. Lehman
#
#
# Demonstrates Model View Controller architecture
#
# Three views are included  (default with buttons, ASCII, and Canvas)
#
# Includes saving data (Options #1 model saves data, Option #2 - module with functions for saving data)
#
#
# TicTacToeModel <---> TicTacToeController <---> TicTacToeView (TicTacToeView_ASCII, TicTacToeView_Canvas)
#         ^
#         |
#         V
#       Save Model              TicTacToeObjectSaver module <---> Save Model
#

from TicTacToeController import TicTacToeController

if __name__ == "__main__":
    
    controller = TicTacToeController()
    controller.run()  # The controller starts the view

