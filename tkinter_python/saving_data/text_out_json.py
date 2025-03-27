# text_out_json.py
# prof. lehman
# spring 2025

# Demonstrates writing data to a JSON file

import json
import os

# Function to write each data entry to a list
def create_entry(name, age, height, scores):
    return {
        "Name": name,
        "Age": age,
        "Height": height,
        "Scores": scores
    }

# --- main ---

# File name
filename = "data.json"

# Sample data stored as a list of dictionaries
data = [
    create_entry("Alice", 25, 5.6, [85, 90, 78]),
    create_entry("Bill", 22, 5.11, [72, 73, 74]),
    create_entry("Carol", 18, 5.8, [82, 83, 85])
]

# Write data to JSON file
with open(filename, mode='w') as file:
    json.dump(data, file, indent=4)  # Pretty-print JSON with indentation

size_bytes = os.path.getsize(filename)
print(f"JSON data saved ({size_bytes} bytes) to {filename}")
