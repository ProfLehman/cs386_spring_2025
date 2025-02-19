# text_out_xml.py
# prof. lehman
# spring 2025

# Demonstrates writing data to an XML file

import os

# Function to write each data item in XML format
def write_entry(file, name, age, height, scores):
    file.write(f"  <Person>\n")
    file.write(f"    <Name>{name}</Name>\n")
    file.write(f"    <Age>{age}</Age>\n")
    file.write(f"    <Height>{height}</Height>\n")
    file.write(f"    <Scores>\n")
    
    # Write each score as an individual XML element
    for score in scores:
        file.write(f"      <Score>{score}</Score>\n")
    
    file.write(f"    </Scores>\n")
    file.write(f"  </Person>\n")

# --- main ---

# Open file for writing
filename = "data.xml"
file = open(filename, mode='w')

# Write XML header and root element
file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
file.write('<People>\n')

# Sample data
write_entry(file, "Alice", 25, 5.6, [85, 90, 78])
write_entry(file, "Bill", 22, 5.11, [72, 73, 74])
write_entry(file, "Carol", 18, 5.8, [82, 83, 85])

# Close root element
file.write('</People>\n')

# Close the file - ensures data is saved
file.close()

size_bytes = os.path.getsize(filename)
print(f"XML data saved ({size_bytes} bytes) to {filename}")
