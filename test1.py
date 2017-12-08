<<<<<<< HEAD
from king import King
from king import Rook


class TxtInterface:
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
=======
from king import King
from king import Rook


class TxtInterface:
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
>>>>>>> 740fcce5396a921e32eb74d68353f55ad13f4973
