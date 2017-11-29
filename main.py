from king import King
import tkinter


class Main:
    def __init__(self):

        # переменные для доски
        self.width = 0
        self.height = 0
        self.matrix = []
        self.active = []
        self.points = []
        self.moves = []
        self.chessmen = []

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
        self.width = 8
        self.height = 8
        for i in range(self.width):
            self.matrix.append([])
            for k in range(self.height):
                self.matrix[i].append(0)

        # отрисовка поля доски
        cell_colors = ["white", "black"]
        cl = 0
        for i in range(self.height):
            for k in range(self.width):
                self.canvas.create_rectangle(50*k, 50*i, 50*k + 50, 50*i + 50, fill=cell_colors[cl])
                if k != self.width-1:
                    cl = not cl
                elif self.width % 2 == 1:
                    cl = not cl

        for i in range(2):
            self.chessmen.append([])

        # инициализация тестовых фигур
        self.matrix[0][0] = King()
        self.matrix[0][0].shape = self.canvas.create_rectangle(10, 10, 40, 40, fill="yellow")
        self.matrix[0][0].coord = [0, 0]
        self.matrix[0][0].set_possible_moves(self.matrix)
        self.chessmen[0].append([0, 0])

        self.matrix[1][1] = King()
        self.matrix[1][1].shape = self.canvas.create_rectangle(60, 60, 90, 90, fill="yellow")
        self.matrix[1][1].coord = [1, 1]
        self.matrix[1][1].set_possible_moves(self.matrix)
        self.chessmen[1].append([1, 1])

        self.matrix[3][3] = King()
        self.matrix[3][3].shape = self.canvas.create_rectangle(160, 160, 190, 190, fill="red")
        self.matrix[3][3].coord = [3, 3]
        self.matrix[3][3].side = 1
        self.matrix[3][3].color = "red"
        self.matrix[3][3].set_possible_moves(self.matrix)
        self.chessmen[1].append([3, 3])

        self.matrix[2][2] = King()
        self.matrix[2][2].shape = self.canvas.create_rectangle(110, 110, 140, 140, fill="red")
        self.matrix[2][2].coord = [2, 2]
        self.matrix[2][2].side = 1
        self.matrix[2][2].color = "red"
        self.matrix[2][2].set_possible_moves(self.matrix)
        self.chessmen[1].append([2, 2])

        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if self.matrix[i][k] != 0:
                    self.matrix[i][k].set_possible_moves(self.matrix)

    # действие при нажатии на фигуру
    def touched(self, event):
        x = event.x//50
        y = event.y//50

        #self.check_the_possibilities()

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
                self.points = []
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
        # собсно перемещение
        self.matrix[x][y] = self.matrix[self.active[0]][self.active[1]]
        self.canvas.delete(self.matrix[self.active[0]][self.active[1]].shape)
        self.matrix[self.active[0]][self.active[1]] = 0
        self.matrix[x][y].shape = self.canvas.create_rectangle(x*50 + 10, y*50 + 10, x*50 + 40, y*50 + 40, fill=self.matrix[x][y].color)
        self.matrix[x][y].coord = [x, y]
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if self.matrix[i][k] != 0:
                    self.matrix[i][k].set_possible_moves(self.matrix)

#    def check_the_possibilities(self):


main = Main()

print(main.matrix)
