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
        print(self.possible_moves)


class Bishop:
    label = "bishop"
    side = 0
    possible_moves = []
