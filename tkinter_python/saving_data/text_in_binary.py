# text_in_binary.py
# prof. lehman
# spring 2025

# Demonstrates reading text, float, int, and a list of ints from a binary file
#
# Character	Type Size (Bytes)
# 'i' Integer (signed) 4
# 'I' Integer (unsigned) 4
# 'f' Float 4
# 'd' Double (float) 8
# 's' String (fixed-length) Variable
# 'c' Character 1

import struct

# Function to read binary data
def read_binary(filename):
    with open(filename, "rb") as file:
        # Read name
        name_length = struct.unpack("I", file.read(4))[0]  # Read name length
        name = file.read(name_length).decode("utf-8")  # Read name data

        # Read integer (age)
        age = struct.unpack("i", file.read(4))[0]

        # Read float (height)
        height = struct.unpack("f", file.read(4))[0]

        # Read list of integers
        list_length = struct.unpack("I", file.read(4))[0]  # Read list length
        scores = []
        for x in range(list_length):
            scores.append( struct.unpack("I", file.read(4))[0] )

    return name, age, height, scores

# Read and display the binary file contents
filename = "data.bin"

for i in range(3):
    name, age, height, scores = read_binary(filename)
    print(f"Loaded Data -> Name: {name}, Age: {age}, Height: {height}, Scores: {scores}")

