from configurations import *

class Coordinate:

    def __init__(self):

        self.width = BRD_WIDTH
        self.height = BRD_HEIGHT
        self.matrix = []
        self.set_initial()

    def set_initial(self):
        for i in range(self.width):
            self.matrix.append([])
            for k in range(self.height):
                self.matrix[i].append(0)

coord = Coordinate()

print(coord.matrix)
