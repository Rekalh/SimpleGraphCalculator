from tkinter import Tk
from tkinter import Canvas
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Event

from Utils import *

import math

class GraphingCalculator:
    x_points = []
    y_points = []

    d_tick = 40
    n_points = 1000

    draw_points = False

    rgb_color = [255, 0, 0]

    window: Tk = None
    canvas: Canvas = None

    window_height, window_width = 0, 0

    def __init__(self, window: Tk, window_width: int, window_height: int):
        self.window, self.window_width, self.window_height = window, window_width, window_height

        self.canvas = Canvas()

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

        self.draw()
        self.draw_ui()

        self.window.bind("<Key>", self.on_key_pressed)

        self.window.mainloop()

    def on_key_pressed(self, e: Event):
        print(f'Pressed key: {e.char}')

    def on_draw_points(self):
        self.draw_points = not self.draw_points
        self.draw()

    def draw(self):
        n_x_ticks = self.window_width // self.d_tick
        n_y_ticks = self.window_height // self.d_tick

        tick_y = (n_y_ticks // 2) * self.d_tick

        # X ticks and X grid
        for i in range(n_x_ticks):
            Line(self.canvas, i * self.d_tick, 0, i * self.d_tick, self.window_height, 210, 210, 210) # X grid
            Line(self.canvas, i * self.d_tick, tick_y - 5, i * self.d_tick, tick_y + 5, 155, 155, 155) # X ticks

        # Y ticks and Y grid
        for i in range(n_y_ticks):
            Line(self.canvas, 0, i * self.d_tick, self.window_width, i * self.d_tick, 210, 210, 210)
            Line(self.canvas, self.window_width / 2 - 5, i * self.d_tick, self.window_width / 2 + 5, i * self.d_tick, 155, 155, 155)

        origin = self.axis_to_screen(0, 0, self.window_width, self.window_height)

        # X axis
        Line(self.canvas, 0, tick_y, self.window_width, tick_y, 155, 155, 155)
        # Y axis
        Line(self.canvas, origin[0], 0, origin[0], self.window_height, 155, 155, 155)

        # Draw points
        if self.draw_points:
            for i in range(len(self.x_points) - 1):
                r_coords = self.axis_to_screen(self.x_points[i], self.y_points[i], self.window_width, self.window_height)
                Point(self.canvas, r_coords[0], r_coords[1], radius=1, r=self.rgb_color[0], g=self.rgb_color[1], b=self.rgb_color[2])

        # Connect the points
        for i in range(len(self.x_points) - 1):
            if i == len(self.x_points) - 1: break
            this = self.axis_to_screen(self.x_points[i], self.y_points[i], self.window_width, self.window_height)
            next = self.axis_to_screen(self.x_points[i + 1], self.y_points[i + 1], self.window_width, self.window_height)

            Line(self.canvas, this[0], this[1], next[0], next[1], r=self.rgb_color[0], g=self.rgb_color[1], b=self.rgb_color[2])

    def draw_ui(self):
        draw_points = BooleanVar()
        Checkbutton(self.window, text="Draw points", variable=draw_points, command=self.on_draw_points).pack()

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
