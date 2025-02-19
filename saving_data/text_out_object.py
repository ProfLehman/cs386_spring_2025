# text_out_object.py
# prof. lehman
# spring 2025

# Demonstrates writing object using pickle

import pickle
import os

# Define a simple class
class Person:
    def __init__(self, name, age, height, scores):
        self.name = name
        self.age = age
        self.height = height
        self.scores = scores

    def __repr__(self):
        return f"Person(Name={self.name}, Age={self.age}, Height={self.height}, Scores={self.scores})"

# Create an object
person1 = Person("Alice", 25, 5.6, [85, 90, 78])

# Save object to a file (Serialization)
filename = "person.pkl"

with open(filename, "wb") as file:
    pickle.dump(person1, file)

size_bytes = os.path.getsize(filename)
print(f"Object data saved ({size_bytes} bytes) to {filename}")


# Load object from file (Deserialization)
#with open("person.pkl", "rb") as file:
#    loaded_person = pickle.load(file)
#
#print("Loaded Object:", loaded_person)
