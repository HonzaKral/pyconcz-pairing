import random

SIZE = 10

def get_neighbors(coordinates):
    x, y = coordinates
    neighbors = []
    for x_offset in (-1, 0, 1):
        x_shifted = x + x_offset
        for y_offset in (-1, 0, 1):
            y_shifted = y + y_offset
            neighbor = (x_shifted, y_shifted)
            if neighbor == coordinates:
                continue
            if -1 in neighbor or SIZE in neighbor:
                continue
            neighbors.append(neighbor)

    return neighbors

def alive_neighbors(grid, coordinates):
    neighbors = get_neighbors(coordinates)
    alive = 0
    for neighbor in neighbors:
        x, y = neighbor
        if grid[x][y]:
            alive += 1

    return alive

def should_live(grid, coordinates):
    alive = grid[coordinates[0]][coordinates[1]]
    live_neighbors = alive_neighbors(grid, coordinates)

    # Live with < 2 : die
    if alive and live_neighbors < 2:
        return False

    # Live with 2 or 3 : live
    if alive and live_neighbors in (2, 3):
        return True

    # Dead with == 3 : live
    if not alive and live_neighbors == 3:
        return True

    # Live with > 3 : die
    if alive and live_neighbors > 3:
        return False


def grid_to_string(grid):
    size = len(grid)
    return '\n'.join(
        ''.join(
            '#' if grid[x][y] else ' '
            for x in range(size)
        ) for y in range(size))



def generate_grid(size=SIZE):
    return [
        [
            random.random() < 0.3
            for _ in range(SIZE)
        ] for _ in range(SIZE)
    ]

def transform_grid(grid):
    size = len(grid)
    new_grid = []
    for x in range(size):
        new_row = []
        for y in range(size):
            new_row.append(should_live(grid, (x, y)))
        new_grid.append(new_row)
    return new_grid

import time
grid = generate_grid()
for _ in range(100):
    print(grid_to_string(grid))
    print('-' * 100)
    grid = transform_grid(grid)
    time.sleep(.2)
