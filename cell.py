from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        ##Left wall
        p1 = Point(x1, y1)
        p2 = Point(x1, y2)

        left_wall = Line(p1, p2)
        if self.has_left_wall == True:
            self.__win.draw_line(left_wall, "black")
        else:
            self.__win.draw_line(left_wall, "white")

        ## Right wall
        p1 = Point(x2, y1)
        p2 = Point(x2, y2)

        right_wall = Line(p1, p2)
        if self.has_right_wall == True:
            self.__win.draw_line(right_wall, "black")
        else:
            self.__win.draw_line(right_wall, "white")

        ## Top wall
        p1 = Point(x1, y1)
        p2 = Point(x2, y1)

        top_wall = Line(p1, p2)
        if self.has_top_wall == True:
            self.__win.draw_line(top_wall, "black")
        else:
            self.__win.draw_line(top_wall, "white")

        ## Bottom wall
        p1 = Point(x1, y2)
        p2 = Point(x2, y2)

        bottom_wall = Line(p1, p2)
        if self.has_bottom_wall == True:
            self.__win.draw_line(bottom_wall, "black")
        else:
            self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):

        if undo == False:
            color = "red"
        else:
            color = "gray"

        xCell = self.__x1 + ((self.__x2 - self.__x1) / 2)
        xToCell = to_cell.__x1 + ((to_cell.__x2 - to_cell.__x1) / 2)

        yCell = self.__y1 + ((self.__y2 - self.__y1) / 2)
        yToCell = to_cell.__y1 + ((to_cell.__y2 - to_cell.__y1) / 2)

        cell = Point(xCell, yCell)
        toCell = Point(xToCell, yToCell)

        move = Line(cell, toCell)
        self.__win.draw_line(move, color)