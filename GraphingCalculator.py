from tkinter import Tk
from tkinter import Canvas
from tkinter import Checkbutton
from tkinter import IntVar

from Utils import *

import math

class GraphingCalculator:
    x_points = []
    y_points = []

    d_tick = 40
    n_points = 1000

    draw_points = False

    rgb_color = [255, 38, 0]

    def __init__(self, window: Tk, window_width, window_height):
        canvas = Canvas()
    
        self.draw_ui(window)

        n_x_ticks = window_width // self.d_tick
        n_y_ticks = window_height // self.d_tick

        tick_y = (n_y_ticks // 2) * self.d_tick

        # X ticks and X grid
        for i in range(n_x_ticks):
            Line(canvas, i * self.d_tick, 0, i * self.d_tick, window_height, 210, 210, 210) # X grid
            Line(canvas, i * self.d_tick, tick_y - 5, i * self.d_tick, tick_y + 5, 155, 155, 155) # X ticks

        # Y ticks and Y grid
        for i in range(n_y_ticks):
            Line(canvas, 0, i * self.d_tick, window_width, i * self.d_tick, 210, 210, 210)
            Line(canvas, window_width / 2 - 5, i * self.d_tick, window_width / 2 + 5, i * self.d_tick, 155, 155, 155)

        origin = self.axis_to_screen(0, 0, window_width, window_height)

        # X axis
        Line(canvas, 0, tick_y, window_width, tick_y, 155, 155, 155)
        # Y axis
        Line(canvas, origin[0], 0, origin[0], window_height, 155, 155, 155)

        # Calculate function outputs
        dx = window_width / self.n_points

        for x in range(0, window_width + 150, int(dx)):
            try:
                a_x = self.screen_to_axis(x, 0, window_width, window_height)[0]
                self.x_points.append(a_x)
                self.y_points.append(self.fn(a_x))
            except:
                self.x_points.remove(a_x)
                continue

        # Draw points
        if self.draw_points:
            for i in range(len(self.x_points) - 1):
                r_coords = self.axis_to_screen(self.x_points[i], self.y_points[i], window_width, window_height)
                Point(canvas, r_coords[0], r_coords[1], radius=1, r=self.rgb_color[0], g=self.rgb_color[1], b=self.rgb_color[2])

        # Connect the points
        for i in range(len(self.x_points) - 1):
            if i == len(self.x_points) - 1: break
            this = self.axis_to_screen(self.x_points[i], self.y_points[i], window_width, window_height)
            next = self.axis_to_screen(self.x_points[i + 1], self.y_points[i + 1], window_width, window_height)

            Line(canvas, this[0], this[1], next[0], next[1], r=self.rgb_color[0], g=self.rgb_color[1], b=self.rgb_color[2])

        window.mainloop()

    def draw_ui(self, window):
        draw_points = IntVar()
        Checkbutton(window, text="Draw points", variable=draw_points, onvalue=True, offvalue=False).pack()
        self.draw_points = draw_points.get()

    # Function to plot
    def fn(self, x):
        return 5 * math.exp(- x ** 2 / 10)

    # Coordinate transformation
    def axis_to_screen(self, x, y, screen_width, screen_height):
        n_x_ticks = screen_width // self.d_tick
        n_y_ticks = screen_height // self.d_tick

        a_x = (x + n_x_ticks // 2) * self.d_tick
        a_y = (n_y_ticks // 2 - y) * self.d_tick

        return a_x, a_y

    def screen_to_axis(self, x, y, screen_width, screen_height):
        n_x_ticks = screen_width // self.d_tick
        n_y_ticks = screen_height // self.d_tick

        s_x = x / self.d_tick - (n_x_ticks // 2)
        s_y = ((n_y_ticks // 2) - y) / self.d_tick

        return s_x, s_y
