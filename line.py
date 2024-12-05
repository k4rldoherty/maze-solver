'''
a line class which a line can be drawn from 2 points 
onto a canvas
'''
class Line:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    def draw(self, canvas, fill_color="black"):
        print(f"Point 1: ({self._point1.x}, {self._point1.y})")
        print(f"Point 2: ({self._point2.x}, {self._point2.y})")
        canvas.create_line(
                    self._point1.x,
                    self._point1.y,
                    self._point2.x,
                    self._point2.y,
                    fill=fill_color,
                    width=2
                )
