import tkinter as tk
from tkinter import Canvas
from Utils import Line, Point

import math

x_points = []
y_points = []

d_tick = 40
n_points = 200

def main():
    window = tk.Tk()

    # Config
    window_width = 1280
    window_height = 720

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window.title("Graphing calculator")
    window.geometry(f'{window_width}x{window_height}+{int((screen_width / 2) - (window_width / 2))}+{int((screen_height / 2) - (window_height / 2))}')

    canvas = Canvas()

    # X ticks and X grid
    n_x_ticks = int(window_width / d_tick)
    for i in range(n_x_ticks):
        Line(canvas, i * d_tick, 0, i * d_tick, window_height, 210, 210, 210)
        Line(canvas, i * d_tick, window_height / 2 - 5, i * d_tick, window_height / 2 + 5, 155, 155, 155)

    # Y ticks and Y grid
    n_y_ticks = int(window_width / d_tick)
    for i in range(n_y_ticks):
        Line(canvas, 0, i * d_tick, window_width, i * d_tick, 210, 210, 210)
        Line(canvas, window_width / 2 - 5, i * d_tick, window_width / 2 + 5, i * d_tick, 155, 155, 155)

    # X axis
    Line(canvas, 0, window_height / 2, window_width, window_height / 2, 155, 155, 155)
    # Y axis
    Line(canvas, window_width / 2, 0, window_width / 2, window_height, 155, 155, 155)

    # Calculate function outputs
    dx = window_width / n_points

    for x in range(0, window_width, int(dx)):
        try:
            a_x = screen_to_axis(x, 0, screen_width, screen_height)[0]
            x_points.append(a_x)
            y_points.append(fn(a_x))
        except:
            x_points.remove(a_x)
            continue

    #Draw points
    for i in range(len(x_points) - 1):
        r_coords = axis_to_screen(x_points[i], y_points[i], window_width, window_height)
        Point(canvas, r_coords[0], r_coords[1], radius=1)

    # Connect the points
    for i in range(len(x_points) - 1):
        if i == len(x_points) - 1: break
        this = axis_to_screen(x_points[i], y_points[i], window_width, window_height)
        next = axis_to_screen(x_points[i + 1], y_points[i + 1], window_width, window_height)

        Line(canvas, this[0], this[1], next[0], next[1], r=0, g=138, b=255)

    window.mainloop()

def fn(x):
    return x ** 2
def axis_to_screen(x, y, screen_width, screen_height):
    a_x = (x * d_tick) + (screen_width / 2)
    a_y = (screen_height / 2) - (y * d_tick)

    return a_x, a_y

def screen_to_axis(x, y, screen_width, screen_height):
    s_x = (x - screen_width / 2) / d_tick
    s_y = ((screen_height / 2) - y) / d_tick

    return s_x, s_y

if __name__ == "__main__":
    main()
