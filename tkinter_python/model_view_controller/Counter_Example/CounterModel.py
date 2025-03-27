# CounterModel.py

# Model
class CounterModel:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
          
    def decrement(self):
        self.count -= 1
        
    def get_value(self):
        return self.count