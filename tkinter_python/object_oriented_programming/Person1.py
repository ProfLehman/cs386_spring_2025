
# Person1.py   (uses "old school" approach)
#
# prof. lehman
# spring 2025
#
# Object Oriented Programming (OOP)
#
# Main way to organize code
#  also used by C++, Java, C#, Swift, PHP, etc...
#
#  + manage complexity
#  + reuse code
#  + more natural way to think about designing code
#
#    objects have data also called properties or attributes
#    that define the object
#
#    objects have methods also called functions
#    that define the actions for what the object can do
#
#    data and methods "encapsulated" together
#
#    each object instance has its own copy of the data
#      but shares the methods
#

class Person:

    # constructor
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age 


    # "getter" for name
    def getName(self):
        return self.name
    
    # "setter" for name
    def setName(self, new_name):
        self.name = new_name
    
    
   # string
    def __str__(self):
        msg = f"{self.name}, {self.age}"
        return msg
    
    # -- end Person class         
    
    
# run this code unless it is being used by another file
if __name__ == "__main__":
    
    jennifer = Person("Jennifer", 21)
    print( jennifer )
    print( jennifer.name ) 
    print( jennifer.age )
    print()

    jennifer.setName("Jenny")
    print( jennifer )
    print( jennifer.getName() )
    
    jennifer.name = "Jen"
    print( jennifer )
    
    jennifer.age = -45
    print( jennifer )
    
    
    
    
    
    
    
    