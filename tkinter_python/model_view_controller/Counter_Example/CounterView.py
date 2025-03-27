import tkinter as tk

# CounterView.py

# GUI View
class CounterView():
    
    #constructor
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        # GUI interface
        self.main = tk.Tk()
        self.main.title("MVC Demo - Counter")
        self.main.geometry("300x100")
        self.main.label = tk.Label(self.main, text="0", font=("Arial", 20))
        self.main.label.pack()
        self.main.button = tk.Button(self.main, text="Increment", command=self.handle_increment)
        self.main.button.pack(side="left",padx=40)
        self.main.button = tk.Button(self.main, text="Decrement", command=self.handle_decrement)
        self.main.button.pack(side="left")
    
    # handle input   
    def run(self):
        self.main.mainloop() #wait for button clicks
    
    # tell controller to process input
    def handle_increment(self):
        self.controller.increment()
    
    def handle_decrement(self):
        self.controller.decrement()

    #  controller will use to update data from model
    def update(self, value):
        self.main.label.config(text=str(value))