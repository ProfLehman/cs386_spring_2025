import os

# text_out_line.py
# prof. lehman
# spring 2025

# Demonstrates writing a text file with one data item per line (no headings)

# Function to write each data item on a separate line
def write_line(file, name, age, height, scores):
    file.write(f"{name}\n")   # Write name
    file.write(f"{age}\n")    # Write age
    file.write(f"{height}\n")  # Write height
    
    # Write each score on a separate line
    for score in scores:
        file.write(f"{score}\n")
    
    #file.write("\n")  # Blank line to separate records

# --- main ---

# Open file for writing
filename = "data.txt"
file = open(filename, mode='w')

# Sample data
write_line(file, "Alice", 25, 5.6, [85, 90, 78])
write_line(file, "Bill", 22, 5.11, [72, 73, 74])
write_line(file, "Carol", 18, 5.8, [82, 83, 85])



# Close the file - ensures data is saved
file.close()

size_bytes = os.path.getsize(filename)
print(f"Text data saved ({size_bytes} bytes) to {filename}")





