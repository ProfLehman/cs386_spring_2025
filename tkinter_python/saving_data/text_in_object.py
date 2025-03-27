# text_in_object.py
# prof. lehman
# spring 2025

# Demonstrates reading object using pickle

import pickle

# Define the same class structure as used during serialization
class Person:
    def __init__(self, name, age, height, scores):
        self.name = name
        self.age = age
        self.height = height
        self.scores = scores

    def __repr__(self):
        return f"Person(Name={self.name}, Age={self.age}, Height={self.height}, Scores={self.scores})"

# File name where the object is stored
filename = "person.pkl"

# Open file and load object (Deserialization)
with open(filename, "rb") as file:
    loaded_person = pickle.load(file)

# Display the loaded object
print("Loaded Object:", loaded_person)
print("Name:", loaded_person.name)
print("Age:", loaded_person.age)
print("Height:", loaded_person.height)
print("Scores:", loaded_person.scores)
