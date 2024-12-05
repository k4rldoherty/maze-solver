import time
from cell import Cell

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows,
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None
            ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self.break_entrance_and_exit()

    def _create_cells(self):
        # Populate matrix
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    # Something is wrong here
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.025)
    
    def break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self._num_rows - 1][self._num_cols -1]

        new_top_left = Cell(
            self._win
        )
        new_top_left.has_top_wall = False
        new_top_left.draw(
            top_left_cell._x1,
            top_left_cell._y1,
            top_left_cell._x2,
            top_left_cell._y2,
        )
        new_bottom_right = Cell(
            self._win
        )
        new_bottom_right.has_bottom_wall = False
        new_bottom_right.draw(
            bottom_right_cell._x1,
            bottom_right_cell._y1,
            bottom_right_cell._x2,
            bottom_right_cell._y2,
        )
    
    # def _break_walls_r(self, i, j):
    #     current_cell = self._cells[i][j]
    #     current_cell.visited = True
    #     while True:
    #         to_visit = []

            