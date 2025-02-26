# xml_out.py
# simplified example writing XML data
# prof. lehman
# spring 2025


import xml.etree.ElementTree as ET

# Sample data
name_value = "John Doe"      # Text from a text field
radio_value = "option1"      # Radio button selection: "option1" or "option2"
checkbox_value = True        # Checkbox value: True or False

# Create the root element
root = ET.Element("data")

# Create and populate child elements
name_elem = ET.SubElement(root, "name")
name_elem.text = name_value

radio_elem = ET.SubElement(root, "radio")
radio_elem.text = radio_value

checkbox_elem = ET.SubElement(root, "checkbox")
checkbox_elem.text = str(checkbox_value)

# Build the XML tree and write it to a file
tree = ET.ElementTree(root)
tree.write("data2.xml", encoding="utf-8", xml_declaration=True)

