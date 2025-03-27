import tkinter as tk

#    Program: deleteGraphicsDemo.py
#     Author: Prof. Lehman
#       Date: 11 February 2025
#
# Description: A simple Tkinter application that provides a canvas for drawing lines and circles.
#              Users can add two lines, two circles, and clear them separately using buttons.
#              Each line and circle is assigned a "tags" value that allows the graphics to be
#              deleted as a group.

class deleteTags:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Canvas")
        
        self.canvas = tk.Canvas(root, width=600, height=500, bg="white")
        self.canvas.pack()
        
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        
        self.draw_lines_btn = tk.Button(btn_frame, text="Draw Lines", command=self.draw_lines)
        self.draw_lines_btn.grid(row=0, column=0)
        
        self.draw_circles_btn = tk.Button(btn_frame, text="Draw Circles", command=self.draw_circles)
        self.draw_circles_btn.grid(row=0, column=1)
        
        self.clear_lines_btn = tk.Button(btn_frame, text="Clear Lines", command=self.clear_lines)
        self.clear_lines_btn.grid(row=0, column=2)
        
        self.clear_circles_btn = tk.Button(btn_frame, text="Clear Circles", command=self.clear_circles)
        self.clear_circles_btn.grid(row=0, column=3)
        
        self.clear_all_btn = tk.Button(btn_frame, text="Clear All", command=self.clear_all)
        self.clear_all_btn.grid(row=0, column=4)
        
    def draw_lines(self):
        # note use of "tags" property to denote group to delete
        self.canvas.create_line(100, 100, 500, 100, fill="orange", width=2, tags="lines")
        self.canvas.create_line(100, 200, 500, 200, fill="brown", width=2, tags="lines")
        self.canvas.create_line(100, 290, 500, 290, fill="red", width=3)
        
    def draw_circles(self):
        # note use of "tags" property to denote group to delete
        self.canvas.create_oval(100, 300, 200, 400, outline="blue", width=2, tags="circles")
        self.canvas.create_oval(250, 300, 350, 400, outline="green", width=2, tags="circles")
        self.canvas.create_oval(450, 300, 550, 400, outline="red", width=3)
        
    def clear_lines(self):
        self.canvas.delete("lines") # delete all graphics with tags "lines"
        
    def clear_circles(self):
        self.canvas.delete("circles") # delete all graphics with tags "circles"
        
    def clear_all(self):
        self.canvas.delete("all") # delete all graphics
        
if __name__ == "__main__":
    root = tk.Tk()
    app = deleteTags(root)
    root.mainloop()
