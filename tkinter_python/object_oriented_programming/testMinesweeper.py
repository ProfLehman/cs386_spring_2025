from MinesweeperDataLogic import Minesweeper


if __name__ == "__main__":
    
    game = Minesweeper(4, 4)


    print("Initial Minesweeper Board:")
    print("0 1 2 3 4 5 6 7")
    print(game.to_string_mines())
    print(game.to_string_board())
    print()
    
    while game.get_status() == "play":
        r, c = map(int, input("Enter row col (0 1): ").split())
        a = int( input("Enter action (0 open, 1 close, 2 flag, 3 question): ") )
        
        game.mark_tile(r, c, a)
        
        print("0 1 2 3 4 5 6 7")
        print(game.to_string_board())
        
    if game.get_status() == "win":
        print("Congratulations! You won the game!")
    else:
        print("Game Over! You hit a mine.")
        print("Final Board:")
        print(game.to_string_mines())

