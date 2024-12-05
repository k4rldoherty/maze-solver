'''
a window class that initializes tkinter as root
a title, a window size
and a canvas which which allows items to be drawn
'''
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, {"bg": "white", "width": width, "height": height})
        self._canvas.pack()
        self._running = False

    def redraw(self):
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)
