
import random

class Grid:
    def __init__(self):
        self.cells = {}

        for x in range(0, 10):

            for y in range(0, 10):
                self.cells[(x, y)] = random.random() < 0.3

    def alive_or_dead(self, cell):
        """
        Given a coordinate of a cell, determine whether it should be alive or
        dead in the next cycle.

        :arg cell: (x, y) coordinate of the cell
        """
        alive = self.cells[cell]
        alive_neighbours = self.neighbour_cells(cell)
        # Live with < 2 : die
        # Live with 2 or 3 : live
        # Dead with == 3 : live
        # Live with > 3 : die

        if alive and alive_neighbours < 2:
            return False
        if alive and (alive_neighbours == 2 or alive_neighbours == 3):
            return True
        if not alive and (alive_neighbours == 3):
            return True
        if alive and (alive_neighbours > 3):
            return False

    def print_grid(self):
        for x in range(10):
            print(''.join('#' if self.cells[(x, y)] else ' ' for y in range(10)))


    def neighbour_cells(self, cell):
        x, y = cell

        neighbour_cells = ( x - 1, y), (x, y - 1), (x + 1, y),(x, y +1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)

        print(neighbour_cells)
        count = 0
        for i in neighbour_cells:
            if i not in self.cells:
                continue

            alive = self.cells[i]
            if alive:
                count = count +1
        return count

g = Grid()
g.print_grid()
