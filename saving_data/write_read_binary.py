# write_read_binary.py
# prof. lehman
# spring 2025

# Demonstrates writing/reading text, float, int to binary file

# Character	Type Size (Bytes)
# 'i' Integer (signed) 4
# 'I' Integer (unsigned) 4
# 'f' Float 4
# 'd' Double (float) 8
# '?' Boolean 1

import struct
import os

filename = "binary_data.bin"
file = open(filename, "wb")

#
# -- int --
#

# save int (i signed, I unsigned)
#value = 2147483641 # max signed int
value = 4294967295 # max unsigned int
# ??? what happens if we try 4294967296

file.write( struct.pack("I", value) ) 


#
# -- float - IEEE float 32 bit
#
# see https://www.h-schmidt.net/FloatConverter/IEEE754.html
#

value = -3.45
file.write( struct.pack("f", value) ) 
#file.write( struct.pack("<f", value) )
#file.write( struct.pack(">f", value) )

# note: < little-endian (least significant byte first)
#       > big-endian (most significant byte first)


#
# -- text --- 
#

# variable-length text
msg = "ABC"
msg_letters = msg.encode("utf-8")
print( msg_letters )

file.write( struct.pack("I", len(msg)) ) 
file.write(msg_letters)  # Write name data

# fixed-length text
msg2 = "abc"
msg2_letters = msg2.encode("utf-8")
file.write( struct.pack("8s", msg2_letters) )


#
# -- binary --- 
#
boolean_value = True
file.write( struct.pack("?", boolean_value ) )



# don't forget to close the file! or data may not save
file.close()

print()
size_bytes = os.path.getsize(filename)
print(f"Binary data saved ({size_bytes} bytes) to {filename}")
print()
print()

# ----------------------------------------------------------

# *** read and display data ***
file = open(filename, "rb")


# Read int
int_value = struct.unpack("I", file.read(4))[0]
print( int_value )


# Read fload
float_value = struct.unpack("f", file.read(4))[0]
print( float_value )


# Read variable-length text
string_length = struct.unpack("I", file.read(4))[0]  # Read length
string = file.read(string_length).decode("utf-8")  # Read data
print( string )

# Read fixed-length text
s = struct.unpack("8s", file.read(8))[0].decode("utf-8").strip('\x00') 
print( s )


# Read boolean
boolean_value = struct.unpack("?", file.read(1))[0]
print( boolean_value )



# note: unpack reads data as a tuple (,)
#       in most cases we want the first item [0]

        
        


