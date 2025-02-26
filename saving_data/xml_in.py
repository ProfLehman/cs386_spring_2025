# xml_in.py
# simplified example reading XML data
# prof. lehman
# spring 2025

import xml.etree.ElementTree as ET

# Specify the XML file name
filename = "data2.xml"

# Parse the XML file and get the root element
tree = ET.parse(filename)
root = tree.getroot()

# Extract the data from the XML elements
name = root.find('name').text
radio = root.find('radio').text
checkbox = root.find('checkbox').text

# Print the extracted values
print("Name:", name)
print("Radio:", radio)
print("Checkbox:", checkbox)


