from tkinter import Tk
from GraphingCalculator import *

def main():
    window = Tk()

    # Config
    window_width = 1280
    window_height = 720

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window.title("Graphing calculator")
    window.geometry(f'{window_width}x{window_height}+{(screen_width // 2) - (window_width // 2)}+{(screen_height // 2) - (window_height // 2)}')

    GraphingCalculator(window, window_width, window_height)

if __name__ == "__main__":
    main()
