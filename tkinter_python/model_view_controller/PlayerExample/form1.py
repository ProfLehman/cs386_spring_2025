
# form1.py
# spring 2025
# prof. lehman
# demonstrates passing data between forms using data class
#
#   form1 <-----------> form2
#     ^                   ^
#     |                   |      
#     ---> GameModel <----
#

import tkinter as tk
from GameModel import GameModel
import form2  # Import the update window

class Form1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form1 - Player Names")
        self.geometry("300x200")
        
        # Create an instance of the game model
        self.model = GameModel()
        
        # Create labels to display the player names
        self.label_player1 = tk.Label(self, text=f"Player 1: {self.model.get_player1()}")
        self.label_player1.pack(pady=5)
        
        self.label_player2 = tk.Label(self, text=f"Player 2: {self.model.get_player2()}")
        self.label_player2.pack(pady=5)
        
        # Create the update button which opens form2.py
        self.btn_update = tk.Button(self, text="Update", command=self.open_update_window)
        self.btn_update.pack(pady=10)
    
    def open_update_window(self):
        # Open the update form as a child window (Toplevel)
        form2.Form2(self, self.model)
    
    def refresh_labels(self):
        # Update the labels to reflect changes in the model
        self.label_player1.config(text=f"Player 1: {self.model.get_player1()}")
        self.label_player2.config(text=f"Player 2: {self.model.get_player2()}")

if __name__ == '__main__':
    app = Form1()
    app.mainloop()
