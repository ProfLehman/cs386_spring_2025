
# Person2.py   (uses "property" approach)
#
# prof. lehman
# spring 2025
#
# demonstrates private variables _name
#  @property and @name.setter
#

class Person:

    # constructor
    def __init__(self, new_name, new_age):
        self._name = new_name  #note simulated "private" _name
        self._age = new_age 


    # "getter" for name
    @property
    def name(self):
        return self._name
 
     # "setter" for name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # "getter" for age
    @property
    def age(self):
        return self._age
 
     # "setter" for age
    @age.setter
    def age(self, new_age):
        if new_age >= 0 and new_age <= 120:
            self._age = new_age
        #else:
        #    print("invalid age")


   # string
    def __str__(self):
        msg = f"{self._name}, {self._age}"
        return msg
    
    # -- end Person class         

    
# run this code unless it is being used by another file
if __name__ == "__main__":
    
    
    alice = Person("Alice", 18)
    ben = Person("Ben", 24)
    
    print( ben._name ) #avoid direct access
    print( ben.name )
    
    ben._name = "Benjamin" #avoid direct access
    ben.name = "Benjamin" 
    
    print( ben )
    
    ben.age = 300
    print( ben )
    
    """
    jennifer = Person("Jennifer", 21)
    print( jennifer )
    print( jennifer.name ) 
    #print( jennifer.age )
    print()

    jennifer.name = "Jen"
    print( jennifer )
    
    jennifer.age = -45
    print( jennifer )
    
    jennifer.age = 45
    print( jennifer )
    """
    
    
    
    
    
