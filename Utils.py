from tkinter import Frame, BOTH

class Line(Frame):
    # Coordinates
    x1, y1, x2, y2 = 0, 0, 0, 0
    canvas = None

    def __init__(self, canvas, x1, y1, x2, y2, r=0, g=0, b=0):
        super().__init__()
        self.x1, self.y1, self.x2, self.y2, self.canvas = x1, y1, x2, y2, canvas
        self.draw_line(r, g, b)

    # Draw a line, given a color
    def draw_line(self, r, g, b):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.get_rgb_hex(r, g, b))
        self.canvas.pack(fill=BOTH, expand=1)

    # Returns hex representation of the r,g,b values provided
    def get_rgb_hex(self, r, g, b):
        s_r = hex(r).replace("0x", "")
        s_g = hex(g).replace("0x", "")
        s_b = hex(b).replace("0x", "")

        if len(s_r) < 2: s_r = "0" + s_r
        if len(s_g) < 2: s_g = "0" + s_g
        if len(s_b) < 2: s_b = "0" + s_b

        return f'#{s_r}{s_g}{s_b}'

class Point(Frame):
    #Coordinates
    x, y = 0, 0
    #Radius
    radius = 0
    canvas = None

    def __init__(self, canvas, x, y, radius=1.5, r=0, g=0, b=0):
        super().__init__()
        self.x, self.y, self.radius, self.canvas = x, y, radius, canvas
        self.draw_point(r, g, b)
    
    #Draw a point, given the color
    def draw_point(self, r, g, b):
        self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.get_rgb_hex(r, g, b))
        self.canvas.pack(fill=BOTH, expand=1)

    # Returns hex representation of the r,g,b values provided
    def get_rgb_hex(self, r, g, b):
        s_r = hex(r).replace("0x", "")
        s_g = hex(g).replace("0x", "")
        s_b = hex(b).replace("0x", "")

        if len(s_r) < 2: s_r = "0" + s_r
        if len(s_g) < 2: s_g = "0" + s_g
        if len(s_b) < 2: s_b = "0" + s_b

        return f'#{s_r}{s_g}{s_b}'
