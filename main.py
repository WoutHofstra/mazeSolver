from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell
from maze import Maze
import sys
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

if __name__ == "__main__":

    num_rows = 12
    num_cols = 18
    margin = 50
    screen_x = 1200
    screen_y = 1000
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved")
    else:
        print("Maze solved!")

    win.wait_for_close()
