import os
import pickle

# TicTacToeModelObjectSaver.py
# spring 2025
# prof. lehman
#
# module contains two functions for saving objects

       
def saveObject(model, filename):
    # Save object to a file (Serialization)

    file = open(filename, "wb")
    pickle.dump( model, file )
    
    size_bytes = os.path.getsize(filename)
    print(f"Object data saved ({size_bytes} bytes) to {filename}")
    
    
def openObject(filename):
    
    model = None
    
    # Open file and load object (Deserialization)
    file = open(filename, "rb")
    model = pickle.load(file)
    
    print( model, "loaded" )
    
    return model
        
        
    
        
        