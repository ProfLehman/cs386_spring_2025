

# US_CAD_Currency.py
# prof. lehman
# spring 2025
#
# currency class demonstrates instance (ie. self) and shared variables
#

class US_CAD_Currency:
    
    # shared variable between classes
    highest_rate = -1
    
    # constructor
    def __init__(self, new_amount, new_rate):
        self.amount = new_amount
        self.rate = new_rate
         
    # getters and setters        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, new_amount):
        if new_amount >= 0.0:
            self._amount = new_amount
        
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, new_rate):
        if new_rate >= 0.0:
            self._rate = new_rate
            if self._rate > US_CAD_Currency.highest_rate:
                US_CAD_Currency.highest_rate = self._rate
            
    # string method __str__
    def __str__(self):
        msg = f"US: ${self.amount:,.2f}"
        msg += f"\nCAN $: {self.convert_to_CAD():,.2f}"
        msg += f"\nUS to CAD rate {self.rate:,.2f}"
        msg += f"\nHighest Rate Seen {US_CAD_Currency.highest_rate}"
        return msg
    
    # other methods
    def convert_to_CAD(self):
        answer = self._amount * self._rate
        return answer

    def highest(self):
        return US_CAD_Currency.highest_rate
    

# run this code unless it is being used by another file
if __name__ == "__main__": 
    
    friday = US_CAD_Currency(100.00, 1.45)
    print( friday )
    print()

    saturday = US_CAD_Currency(100.00, 4.45)
    print( saturday )
    print()

    friday.rate = 1.32
    print( friday )
    print()

    friday.amount = 23.45
    print( friday )
    print()






