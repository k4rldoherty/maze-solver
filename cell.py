'''
each cell is a box with 4 potential walls in the maze
the window is made up of multiple cells
It should know which walls it has, 
where it exists on the canvas in x/y coordinates, 
and access to the window so that it can draw itself.
'''
from point import Point
from line import Line

class Cell:
    def __init__(
            self,
            win
        ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(
            self,
            x1, y1, x2, y2,
            fill_color="black"
        ):
        '''
        If the cell has a left wall, draw it.
        If the cell has a top wall, draw it, and so on and so forth for each

        '''
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(line, fill_color)
        else:
            self._win.draw_line(line, "white")
            
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line, fill_color)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line, fill_color)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(line, fill_color)
        else:
            self._win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)






