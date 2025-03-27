

# form2.py
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
class Form2(tk.Toplevel):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.parent = parent  # Reference to form1 instance
        self.model = model
        self.title("Form2 - Update Player Names")
        self.geometry("300x200")
        
        # Label and entry for Player 1
        tk.Label(self, text="Player 1 Name:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_player1 = tk.Entry(self)
        self.entry_player1.grid(row=0, column=1, padx=10, pady=5)
        self.entry_player1.insert(0, self.model.get_player1())
        
        # Label and entry for Player 2
        tk.Label(self, text="Player 2 Name:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_player2 = tk.Entry(self)
        self.entry_player2.grid(row=1, column=1, padx=10, pady=5)
        self.entry_player2.insert(0, self.model.get_player2())
        
        # Save button to update the model and refresh form1
        self.btn_save = tk.Button(self, text="Save", command=self.save)
        self.btn_save.grid(row=2, column=0, columnspan=2, pady=10)
    
    def save(self):
        # Retrieve new names from the entries
        new_player1 = self.entry_player1.get()
        new_player2 = self.entry_player2.get()
        
        # Update the model using setters
        self.model.set_player1(new_player1)
        self.model.set_player2(new_player2)
        
        # Refresh the labels in the parent window (form1)
        self.parent.refresh_labels()
        
        # Close the update window
        self.destroy()
