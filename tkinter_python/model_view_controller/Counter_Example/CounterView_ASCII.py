# CounterView_ASCII.py

# ASCII View
class CounterView_ASCII():

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
    #  controller will use to update data from model
    def update(self, value):
        print(f"Counter: {value}")
        
    # handle input
    def run(self):
        print("starting ASCII ...")
        while True:
            action = input("Enter action (+ add, - sub, q quit): ")
            
            if action == "q":
                break # I know crazy to see Prof. Lehman using a break :-)
            elif action == "+":
                self.controller.increment()                    
            elif action == "-":
                self.controller.decrement()        
            else:
                print("Error: invalid action")
                           
                