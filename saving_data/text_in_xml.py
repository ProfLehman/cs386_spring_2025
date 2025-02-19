# text_in_xml.py
# prof. lehman
# spring 2025

# Demonstrates reading an XML file and displaying data

import xml.etree.ElementTree as ET

# --- main ---

# File name
filename = "data.xml"

# Parse the XML file
tree = ET.parse(filename)
root = tree.getroot()

# Process each person entry
for person in root.findall("Person"):
    
    name = person.find("Name").text
    age = int(person.find("Age").text)
    height = float(person.find("Height").text)
    
    # Read scores as a list of integers
    scores = [int(score.text) for score in person.find("Scores").findall("Score")]
    
    # Display data
    print(f"Name: {name}, Age: {age}, Height: {height}, Scores: {scores}")
