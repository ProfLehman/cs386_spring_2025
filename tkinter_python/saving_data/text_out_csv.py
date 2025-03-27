# text_out_csv.py
# prof. lehman
# spring 2025

# demonstrates writing csv file
# CSV => comma separated values
# files can be created/opened with most spreadsheets

import os

# function to write single line of CSV data
def write_line( file, name, age, height, scores ):
    
    file.write(f"{name},{age},{height},")  # write non-list values

    file.write( f"{scores[0]}," ) # write data from list
    file.write( f"{scores[1]}," )    
    file.write( f"{scores[2]}" )
    file.write("\n")    
    

# --- main ---

# open file for writing
filename = "data.csv"
file = open(filename, mode='w')

# Write header
file.write("Name,Age,Height,Score1,Score2,Score3\n")


# Sample data
name = "Alice"
age = 25
height = 5.6
scores = [85, 90, 78]  # List of scores

# write data using function
write_line( file, name, age, height, scores )
write_line( file, "Bill", 22, 5.11, [72, 73, 74] )
write_line( file, "Carol", 18, 5.8, [82, 83, 85] )


# close the file - ensures data saved
file.close()


size_bytes = os.path.getsize(filename)
print(f"CSV data ({size_bytes} bytes) saved to {filename}")
