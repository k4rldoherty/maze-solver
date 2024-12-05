from window import Window
from cell import Cell
from maze import Maze

def main():
    num_rows = 12
    num_cols = 12
    margin = 50
    width = 800
    height = 600
    win = Window(800, 600)
    cell_size_x = (width - 2 * margin) / num_cols
    cell_size_y = (height - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()

main()
