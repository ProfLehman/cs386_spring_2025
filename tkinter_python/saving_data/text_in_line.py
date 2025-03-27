# text_in_line.py
# prof. lehman
# spring 2025

# Demonstrates reading a text file with one data item per line
# by reading data into a list, then processing data from list

# --- main ---

# File name
filename = "data.txt"

# Open file for reading
file = open(filename, mode='r')

lines = file.readlines()

i = 0  # skip line 0 which is heading
while i < len(lines):
    
    name = lines[i].strip()  # name
    
    age = int( lines[i+1].strip() )  # age converted to int
    
    height = float( lines[i+2].strip() )  # height converted to float

    scores = []
    for s in range(3,6):
        scores.append( int( lines[i+s].strip() ) )  # score converted to int

    # Display data
    print(f"Name: {name}, Age: {age}, Height: {height}, Scores: {scores}")

    i = i + 6
    
# Close the file
file.close()
