# text_in_csv.py
# prof. lehman
# spring 2025

# Demonstrates reading CSV file and displaying data

# --- main ---

# File name
filename = "data.csv"

# Open file for reading
file = open(filename, mode='r')

# Read the header line
header = file.readline().strip()
print(header)  # Display header

# Read and display each line of data
for line in file:

    values = line.strip().split(",")  # Split CSV values

    name = values[0]
    age = int(values[1])  # Convert age to integer
    height = float(values[2])  # Convert height to float

    scores = []
    scores.append( int(values[3]) )
    scores.append( int(values[4]) )
    scores.append( int(values[5]) )
                   
    # Display data
    print(f"Name: {name}, Age: {age}, Height: {height}, Scores: {scores}")

# Close the file
file.close()
