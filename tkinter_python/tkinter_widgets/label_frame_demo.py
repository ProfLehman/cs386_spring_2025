
# LabelFrame.py
# demonstrates LabelFrames

import tkinter as tk

root = tk.Tk()
root.title("Example of LabelFrame")

# Create a LabelFrame for grouping related widgets
frame = tk.LabelFrame(root, text="Options", padx=5, pady=5)
frame.pack(padx=10, pady=10)

# Add some widgets to the LabelFrame
tk.Checkbutton(frame, text="Option 1").pack(anchor='w')
tk.Checkbutton(frame, text="Option 2").pack(anchor='w')

root.mainloop()
