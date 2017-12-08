<<<<<<< HEAD
class King:
    label = 'king'
    side = 0

    coord = []
    possible_moves = []
    blocking_moves = []
    def set_possible_moves(self, matrix_copy):
        self.possible_moves = []
        for i in range(9):
            x = i % 3 - 1
            y = i // 3 - 1
            x = self.coord[0] + x
            y = self.coord[1] + y
            if x >= 0 and x < len(matrix_copy):
                if y >= 0 and y < len(matrix_copy):
                    if [x, y] != self.coord:
                        if matrix_copy[x][y] == 0:
                            self.possible_moves.append([x, y])
                        elif matrix_copy[x][y].side != self.side:
                            self.possible_moves.append([x, y])


class Bishop:
    label = "bishop"
    side = 0
    possible_moves = []


class Rook:
    label = "rook"
    side = 0

    coord = []
    possible_moves = []
    blocking_moves = []

    def set_possible_moves(self, matrix_copy):
        self.possible_moves = []
        self.blocking_moves = []

        counter = 0
        for i in range(len(matrix_copy[1]) - self.coord[1] - 1):
            if matrix_copy[self.coord[0]][self.coord[1]+i+1] != 0:
                if matrix_copy[self.coord[0]][self.coord[1]+i+1].side != self.side:
                    if counter == 0:
                        self.possible_moves.append([self.coord[0], self.coord[1]+i+1])
                        counter += 1
                        print(self.coord[1]+i+1)
                    elif counter == 1:
                        self.blocking_moves.append([self.coord[0], self.coord[1] + i + 1])
                        counter += 1
                    print([self.coord[0], self.coord[1]+i+1])
                else:
                    counter = 2
            else:
                if counter == 0:
                    self.possible_moves.append([self.coord[0], self.coord[1] + i + 1])
                if counter == 1:
                    self.blocking_moves.append([self.coord[0], self.coord[1] + i + 1])

        counter = 0
        for i in range(self.coord[1]):
            if matrix_copy[self.coord[0]][self.coord[1]-i-1] != 0:
                if matrix_copy[self.coord[0]][self.coord[1]-i-1].side != self.side:
                    if counter == 0:
                        self.possible_moves.append([self.coord[0], self.coord[1]-i-1])
                        counter += 1
                    elif counter == 1:
                        self.blocking_moves.append([self.coord[0], self.coord[1]-i-1])
                        counter += 1
                else:
                    counter = 2
            else:
                if counter == 0:
                    self.possible_moves.append([self.coord[0], self.coord[1]-i-1])
                if counter == 1:
                    self.blocking_moves.append([self.coord[0], self.coord[1]-i-1])

        for i in range(len(matrix_copy) - self.coord[0] - 1):
            if matrix_copy[self.coord[0] + i + 1][self.coord[1]] != 0:
                if matrix_copy[self.coord[0] + i + 1][self.coord[1]].side != self.side:
                    if counter == 0:
                        self.possible_moves.append([self.coord[0] + i + 1, self.coord[1]])
                        counter += 1
                    elif counter == 1:
                        self.blocking_moves.append([self.coord[0] + i + 1, self.coord[1]])
                        counter += 1
                else:
                    counter = 2
            else:
                if counter == 0:
                    self.possible_moves.append([self.coord[0] + i + 1, self.coord[1]])
                if counter == 1:
                    self.blocking_moves.append([self.coord[0] + i + 1, self.coord[1]])

        for i in range(self.coord[0]):
            if matrix_copy[self.coord[0] - i - 1][self.coord[1]] != 0:
                if matrix_copy[self.coord[0] - i - 1][self.coord[1]].side != self.side:
                    if counter == 0:
                        self.possible_moves.append([self.coord[0] - i - 1, self.coord[1]])
                        counter += 1
                    elif counter == 1:
                        self.blocking_moves.append([self.coord[0] - i - 1, self.coord[1]])
                        counter += 1
                else:
                    counter = 2
            else:
                if counter == 0:
                    self.possible_moves.append([self.coord[0] - i - 1, self.coord[1]])
                if counter == 1:
                    self.blocking_moves.append([self.coord[0] - i - 1, self.coord[1]])
=======
class King:
    label = 'king'
    side = 0
    color = "yellow"

    coord = []
    possible_moves = []
    def set_possible_moves(self, matrix_copy):
        self.possible_moves = []
        for i in range(9):
            x = i % 3 - 1
            y = i // 3 - 1
            x = self.coord[0] + x
            y = self.coord[1] + y
            if x >= 0 and x < len(matrix_copy):
                if y >= 0 and y < len(matrix_copy):
                    if [x, y] != self.coord:
                        if matrix_copy[x][y] == 0:
                            self.possible_moves.append([x, y])
                        elif matrix_copy[x][y].side != self.side:
                            self.possible_moves.append([x, y])


class Bishop:
    label = "bishop"
    side = 0
    possible_moves = []


class Rook:
    label = "rook"
    side = 0
    color = "yellow"

    coord = []
    possible_moves = []
    check_moves = []

    def set_possible_moves(self, matrix_copy):
        self.possible_moves = []

        counter = 0
        for i in range(len(matrix_copy[0]) - self.coord[1] - 1):
            self.possible_moves.append([self.coord[0], self.coord[1]+i+1])
        for i in range(self.coord[1]):
            self.possible_moves.append([self.coord[0], self.coord[1]-i-1])
        for i in range(len(matrix_copy) - self.coord[0] - 1):
            self.possible_moves.append([self.coord[0] + i + 1, self.coord[1]])
        for i in range(self.coord[0]):
            self.possible_moves.append([self.coord[0] - i - 1, self.coord[1]])
>>>>>>> 740fcce5396a921e32eb74d68353f55ad13f4973
