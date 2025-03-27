# text_out_binary.py
# prof. lehman
# spring 2025

# Demonstrates writing text, float, int, and a list of ints in a binary file

# Character	Type Size (Bytes)
# 'i' Integer (signed) 4
# 'I' Integer (unsigned) 4
# 'f' Float 4
# 'd' Double (float) 8
# 's' String (fixed-length) Variable
# 'c' Character 1

import struct
import os

# Function to write binary data
def write_binary(filename, name, age, height, scores):
    with open(filename, "ab") as file:
        # Write text (convert string to bytes and store length)
        name_bytes = name.encode("utf-8")  # Convert string to bytes
        file.write(struct.pack("I", len(name_bytes)))  # Write name length (unsigned int)
        file.write(name_bytes)  # Write name data

        # Write integer (age)
        file.write(struct.pack("i", age))  # 'i' for signed integer

        # Write float (height)
        file.write(struct.pack("f", height))  # 'f' for float

        # Write list of integers
        file.write(struct.pack("I", len(scores)))  # Write list length
        for score in scores:
            file.write(struct.pack("i", score))  # Write each score as integer

# Sample data
filename = "data.bin"

write_binary(filename, "Alice", 25, 5.6, [85, 90, 78])
write_binary(filename, "Bill", 22, 5.11, [72, 73, 74])
write_binary(filename, "Carol", 18, 5.8, [82, 83, 85])


size_bytes = os.path.getsize(filename)
print(f"Binary data saved ({size_bytes} bytes) to {filename}")
