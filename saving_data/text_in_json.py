# text_in_json.py
# prof. lehman
# spring 2025

# Demonstrates reading a JSON file and displaying data

import json

# --- main ---

# File name
filename = "data.json"

# Open and read the JSON file
with open(filename, mode='r') as file:
    data = json.load(file)  # Load JSON content into a Python list of dictionaries

# Process and display data
for person in data:
    name = person["Name"]
    age = person["Age"]
    height = person["Height"]
    scores = person["Scores"]  # List of scores
    
    print(f"Name: {name}, Age: {age}, Height: {height}, Scores: {scores}")
