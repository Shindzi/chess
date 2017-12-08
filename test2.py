import math

class PossibilitiesTest:
    def check_king_state(self, matrix_copy, turn):
        coord = []
        hazard = []
        for i in range(len(matrix_copy)):
            for k in range(len(matrix_copy)):
                if matrix_copy[i][k] != 0:
                    if matrix_copy[i][k].label == 'king' and matrix_copy[i][k].side == turn:
                        coord = matrix_copy[i][k].coord
        if coord != []:
            for i in range(len(matrix_copy)):
                for k in range(len(matrix_copy)):
                    if matrix_copy[i][k] != 0:
                        if matrix_copy[i][k].label != 'king':
                            for o in range(len(matrix_copy[i][k].possible_moves)):
                                if matrix_copy[i][k].possible_moves[o] == [coord[0], coord[1]]:
                                    hazard.append([i, k])
        self.check_possibilities(matrix_copy, coord, hazard, turn)

    def check_possibilities(self, matrix_copy, coord, hazard, turn):
        revised_possible_moves = []
        the_threatening_line = []


        # while len(the_threatening_line) != matrix_copy[coord[0]][coord[1]]

        if hazard != []:
            if len(hazard) > 0:

                if len(hazard) == 1:
                    self.calculate_the_line(coord, hazard)

                for i in range(len(matrix_copy)):
                    for k in range(len(matrix_copy[0])):
                        if matrix_copy[i][k] != 0:
                            if matrix_copy[i][k].side == turn:
                                if len(hazard) == 1:
                                    for o in matrix_copy[i][k].possible_moves:
                                        print()
                                matrix_copy[i][k].possible_moves = []

    def calculate_the_line(self, coord, hazard):
        revised_possible_moves = []
        if coord[0] - hazard[0][0] == 0:
            for i in range(int(math.fabs(hazard[0][1] - coord[1]))):
                revised_possible_moves.append([coord[0], coord[1] + (i+1)*int(math.copysign(1, hazard[0][1] - coord[1]) )])
        elif coord[1] - hazard[0][1] == 0:
            for i in range(int(math.fabs(hazard[0][0] - coord[0]))):
                revised_possible_moves.append([coord[0] + (i+1)*int(math.copysign(1, hazard[0][0] - coord[0]) ), coord[1]])


           # for i in range(int(math.fabs(coord[1] - hazard[0][1] - 1))):
            #    revised_possible_moves.append([coord[0], int(coord[1] + math.copysign(1, coord[1] - hazard[0][1]))])
        print(revised_possible_moves)
