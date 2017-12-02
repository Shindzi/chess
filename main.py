from king import King
from king import Rook
from test1 import TxtInterface
import tkinter


class Main:
    def __init__(self):
        self.t_inter = TxtInterface()

        # переменные для доски
        self.matrix = []
        self.active = []
        self.moves = []
        self.colors = ["yellow", "red", "blue"]

        # холст
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master, width=500, height=400)
        self.canvas.pack()

        # запуск системы MAGI
        self.turn = 0
        self.set_initial()
        self.canvas.bind("<Button-1>", self.touched)
        self.master.mainloop()

    # инициализация основных переменных. Можно было и в __init__, но я ступил
    def set_initial(self):
        # инициализация переменных доски
        self.matrix = self.t_inter.get_the_matrix()

        # отрисовка поля доски
        cell_colors = ["white", "black"]
        cl = 0
        # len(self.matrix) - ширина
        # len(self.matrix[0]) - высота
        for i in range(len(self.matrix[0])):
            for k in range(len(self.matrix)):
                self.canvas.create_rectangle(50*k, 50*i, 50*k + 50, 50*i + 50, fill=cell_colors[cl])
                if k != len(self.matrix[0])-1:
                    cl = not cl
                elif len(self.matrix) % 2 == 1:
                    cl = not cl

        # инициализация тестовых фигур
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if self.matrix[i][k] != 0:
                    self.matrix[i][k].shape = self.canvas.create_rectangle(i * 50 + 10,
                                                                                         k * 50 + 10,
                                                                                         i * 50 + 40,
                                                                                         k * 50 + 40,
                                                                           fill=self.colors[self.matrix[i][k].side])
                    self.matrix[i][k].set_possible_moves(self.matrix)

    def get_the_matrix(self):
        file = open('resource.txt')

        c = 0
        width = 0
        cm = ''
        matrix = []

        for line in file:
            if c == 0:
                width = int(line)

            if c == 1:
                for i in range(width):
                    matrix.append([])
                    for k in range(int(line)):
                        matrix[i].append(0)
            if c == 2:
                cm = line
                for i in range(cm.count(';')):
                    name = ''
                    side = ''
                    coord = ['', '']

                    for k in range(cm.find(';')):
                        if name == '':
                            name = cm[0]
                        elif side == '':
                            side = cm[0]
                        elif type(coord[0]) is str:
                            if cm[0] == ',':
                                coord[0] = int(coord[0])
                            else:
                                coord[0] += cm[0]
                        else:
                            coord[1] += cm[0]
                        cm = cm[1:]
                    cm = cm[1:]

                    coord[1] = int(coord[1])

                    if name == 'k':
                        matrix[int(coord[0])][coord[1]] = King()
                    if name == 'r':
                        matrix[int(coord[0])][coord[1]] = Rook()
                    matrix[int(coord[0])][coord[1]].side = int(side)
                    matrix[int(coord[0])][coord[1]].coord = coord
            c += 1
        return matrix

    # действие при нажатии на фигуру
    def touched(self, event):
        x = event.x//50
        y = event.y//50

        # self.check_the_possibilities()

        # условие: не является ли указанный квадрат пустым
        if self.matrix[x][y] != 0:
            if self.matrix[x][y].side == self.turn:

                # адрес фигуры, которую предполагается двигать
                self.active = [x, y]

                # массив с адресами всех возможных для активной фигуры ходов
                self.moves = self.matrix[x][y].possible_moves

                # отрисовка квадратов-индикаторов возможных ходов
                # таким образом, чтобы его можно было удалить,
                # обратившись к элементу массива.
                # потом удаление по-другому сделаю
                for i in range(len(self.moves)):
                    self.canvas.create_oval(self.moves[i][0]*50 + 20, self.moves[i][1]*50 + 20, self.moves[i][0]*50 + 30, self.moves[i][1]*50 + 30, tag="oval", fill="blue")

                # привязка функции при указании места, куда надо передвигать
                self.canvas.bind("<Button-1>", self.pointed)

    # действие при указании на точку перемещения
    def pointed(self, event):
        # хрень смотрит, возможно ли перемещение
        # активной фигуры на указанный квадрат
        for i in range(len(self.moves)):
            if self.moves[i] == [event.x//50, event.y//50]:

                self.move(event.x//50, event.y//50)
                # передача ходу другому игроку
                self.turn = not self.turn

        self.canvas.delete("oval")

        # если нет, то просто возвращается в
        # ожидание очередного клика на новую
        # фигуру

        self.canvas.bind("<Button-1>", self.touched)

    # перемещение фигуры
    def move(self, x, y):

        if self.matrix[x][y] != 0:
            self.canvas.delete(self.matrix[x][y].shape)
            self.matrix[x][y] = 0

        # собсно перемещение
        self.matrix[x][y] = self.matrix[self.active[0]][self.active[1]]
        self.canvas.delete(self.matrix[self.active[0]][self.active[1]].shape)
        self.matrix[self.active[0]][self.active[1]] = 0
        self.matrix[x][y].shape = self.canvas.create_rectangle(x*50 + 10, y*50 + 10, x*50 + 40, y*50 + 40,
                                                               fill=self.colors[self.matrix[x][y].side])
        self.matrix[x][y].coord = [x, y]
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if self.matrix[i][k] != 0:
                    self.matrix[i][k].set_possible_moves(self.matrix)

#    def check_the_possibilities(self):


main = Main()
