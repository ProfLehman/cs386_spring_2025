# MinesweeperDataLogic.py
# prof. lehman
# spring 2025
#
# Used ChatGPT 40 to convvert minesweeper.cs to python
#
# spring 2009 (spring 2011, spring 2013)
# converted to c# spring 2015
# minesweeper class supports underlying data for
# a minesweeper game
# used as coding assignment in C# for CS 286 Visual Programming Sample Solution
#
# original work based on Nifty Assignment presentation http://nifty.stanford.edu/2004/LehmanMinesweeper/
#

import random

class Minesweeper:
    def __init__(self, rows=8, cols=8):
        self._rows = rows
        self._cols = cols
        self._mines = [[0 for _ in range(cols)] for _ in range(rows)]
        self._tiles = [[1 for _ in range(cols)] for _ in range(rows)]  # 1: closed, 0: open, 2: flagged, 3: question
        self._status = "play"
        self._num_mines = max(1, (rows * cols) // 10)  # Ensure at least 1 mine
        self._place_mines()
        self._calculate_clues()
    
    def get_status(self):
        return self._status
    
    def get_rows(self):
        return self._rows
    
    def get_cols(self):
        return self._cols
    
    def mark_tile(self, r, c, tile_type):
        if self._is_valid_index(r, c):
            if tile_type == 0:  # Open
                if self._mines[r][c] == 0:
                    self._open_adjacent_blanks(r, c)
                else:
                    self._tiles[r][c] = 0
                    if self._mines[r][c] == 9:
                        self._status = "lose"
                    elif self.game_won():
                        self._status = "win"
            elif tile_type in (1, 2, 3) and self._tiles[r][c] != 0:
                self._tiles[r][c] = tile_type
    
    def to_string_mines(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self._mines)
    
    def to_string_tiles(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self._tiles)
    
    def to_string_board(self):
        board = []
        for r in range(self._rows):
            row = []
            for c in range(self._cols):
                if self._status == "play":
                    if self._tiles[r][c] == 0:
                        row.append(str(self._mines[r][c]) if self._mines[r][c] > 0 else " ")
                    elif self._tiles[r][c] == 1:
                        row.append("X")
                    elif self._tiles[r][c] == 2:
                        row.append("F")
                    else:
                        row.append("?")
                elif self._status == "win":
                    row.append("F" if self._mines[r][c] == 9 else str(self._mines[r][c]) if self._mines[r][c] > 0 else " ")
                elif self._status == "lose":
                    if self._mines[r][c] == 9:
                        row.append("!" if self._tiles[r][c] == 0 else "*")
                    elif self._tiles[r][c] == 2:
                        row.append("F" if self._mines[r][c] == 9 else "-")
                    else:
                        row.append("X" if self._tiles[r][c] == 1 else "?")
            board.append(" ".join(row))
        return "\n".join(board)
    
    def _place_mines(self):
        placed = 0
        while placed < self._num_mines:
            r, c = random.randint(0, self._rows - 1), random.randint(0, self._cols - 1)
            if self._mines[r][c] != 9:
                self._mines[r][c] = 9
                placed += 1
    
    def _calculate_clues(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(self._rows):
            for c in range(self._cols):
                if self._mines[r][c] == 9:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if self._is_valid_index(nr, nc) and self._mines[nr][nc] != 9:
                            self._mines[nr][nc] += 1
    
    def _is_valid_index(self, r, c):
        return 0 <= r < self._rows and 0 <= c < self._cols
    
    def game_won(self):
        for r in range(self._rows):
            for c in range(self._cols):
                if self._tiles[r][c] != 0 and self._mines[r][c] != 9:
                    return False
        return True
    
    def _open_adjacent_blanks(self, r, c):
        if not self._is_valid_index(r, c) or self._tiles[r][c] == 0:
            return
        if self._mines[r][c] == 0:
            self._tiles[r][c] = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                self._open_adjacent_blanks(r + dr, c + dc)
        elif 1 <= self._mines[r][c] <= 8:
            self._tiles[r][c] = 0

# Example Usage
# run this code unless it is being used by another file
if __name__ == "__main__": 

    game = Minesweeper(28, 28)

    print("Mines:")
    print(game.to_string_mines())
    print()

    print("Tiles:")
    print(game.to_string_tiles())
    print()

    print("Initial Board:")
    print(game.to_string_board())
    print()
    
    r = int( input("Enter row: ") )
    c = int( input("Enter col: ") )

    game.mark_tile( r, c, 0)
    
    print( game.get_status() )
    print(game.to_string_board())
    print()
