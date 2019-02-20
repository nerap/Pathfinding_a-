import math

class Cell:

    def __init__(self, coords, coords_parent, parent_cell_g_cost, end):
        self.coord = coords
        self.coord_parent = coords_parent
        self.discovered = False
        self.calcul_g_cost(parent_cell_g_cost)
        self.calcul_h_cost(end)

    def get_f_cost(self):
        return self.g_cost + self.h_cost

    def get_g_cost(self):
        return self.g_cost

    def set_g_cost(self, g):
        self.g_cost = g

    def get_h_cost(self):
        return self.h_cost

    def set_h_cost(self, h):
        self.h_cost = h
        
    def get_printed(self):
        return self.printed

    def set_printed(self, p):
        self.printed = p

    def get_discovered(self):
        return self.discovered

    def set_discovered(self, bool):
        self.discovered = bool

    def get_coord(self):
        return self.coord

    def get_coord_parent(self):
        return self.coord_parent

    def calcul_g_cost(self, start):
        self.set_g_cost(int(math.sqrt(((start[1] - self.get_coord()[1]) ** 2) + ((start[0] - self.get_coord()[0]) ** 2))*10))


    def calcul_h_cost(self, end):
        self.set_h_cost(int(math.sqrt(((end[1] - self.get_coord()[1]) ** 2) + ((end[0] - self.get_coord()[0]) ** 2))*10))
