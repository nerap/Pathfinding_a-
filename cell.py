import math

class Cell:

    def __init__(self, coords, coords_parent, parent_cell_g_cost, end):
        """After a cell get discovered we need to initialize it

        coords : List [int,int], the actual coordinate of the cell to initialize
        coords_parent : List [int, int] the parent coordinate of the cell
        parent_cell_g_cost : Int, the g_cost of the parent
        end : List [int, int], the coords of the end point
        """
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

    def get_discovered(self):
        return self.discovered

    def set_discovered(self, bool):
        self.discovered = bool

    def get_coord(self):
        return self.coord

    def get_coord_parent(self):
        return self.coord_parent

    def calcul_g_cost(self, parent_cell_g_cost):
        """Based on the parent cell, this function will set the g_cost of a cell
        parent_cell_g_cost: the g_cost of cell depends on the parent cell
        """
        if self.get_coord_parent()[0] != self.get_coord()[0] and self.get_coord_parent()[1] != self.get_coord()[1]:
            self.set_g_cost(parent_cell_g_cost + 14)
        else:
            self.set_g_cost(parent_cell_g_cost + 10)

    def calcul_h_cost(self, end):
        """Based on the end coords, will set de h_cost of the cell
        end: List[int, int] = the actual coord of the end point

        """
        self.set_h_cost(int(math.sqrt(((end[1] - self.get_coord()[1]) ** 2) + ((end[0] - self.get_coord()[0]) ** 2))))
