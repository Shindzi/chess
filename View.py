from configurations import *
import Coordinate as C
import tkinter

class View():
    def __init__(self):

        self.master = tkinter.Tk()

        self.create_chess_base()
        self.master.mainloop()

    def create_chess_base(self):
        self.create_canvas()
        self.draw_board()

    def create_canvas(self):
        canvas_width = BRD_WIDTH * CELL_SIZE
        canvas_height = BRD_HEIGHT * CELL_SIZE
        self.canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
        self.canvas.pack()

    def draw_board(self):
        height = BRD_HEIGHT
        width = BRD_WIDTH
        cl = 0
        for i in range(height):
            for k in range(width):
                self.canvas.create_rectangle(50*k, 50*i, 50*k + 50, 50*i + 50, fill=cell_colors[cl])
                if k != width-1:
                    cl = not cl
                elif width % 2 == 1:
                    cl = not cl

board = View()
