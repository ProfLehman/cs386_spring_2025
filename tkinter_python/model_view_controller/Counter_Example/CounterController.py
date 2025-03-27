from CounterModel import CounterModel
from CounterView import CounterView
from CounterView_ASCII import CounterView_ASCII

# CounterController.py

# Controller
class CounterController:
    def __init__(self):
        # controller has an instance of the model
        self.model = CounterModel()
        
        # controller has an instance of the view
        # pick *one* of the View's
        self.view = CounterView(self)
        #self.view = CounterView_ASCII(self)
    
    def increment(self):
        self.model.increment()
        self.view.update(self.model.get_value())

    def decrement(self):
        self.model.decrement()
        self.view.update(self.model.get_value())
        
    def run(self):
        self.view.run()