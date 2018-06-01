from PIL import Image

def get_neighbours(coordinates):
    x, y = coordinates
    neighbors = []
    for xo in (-1, 0, 1):
        for yo in (-1, 0, 1):
            neighbor = (x + xo, y + yo)
            if neighbor != (x, y):
                neighbors.append(neighbor)
    return neighbors


def get_alive_neighbors(grid, coordinates):
    all_neighbours = get_neighbours(coordinates)
    alive_cells = []
    for n in all_neighbours:
        if grid.get(n, False):
            alive_cells.append(n)
    return len(alive_cells)

"""
Any live cell with fewer than two live neighbors dies, as if by under population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

def should_live(grid, coordinates):
    n = get_alive_neighbors(grid, coordinates)

    return 1 < n < 4 if grid[coordinates] else n == 3

def evolve(grid):
    return {
        k: should_live(grid, k) for k in grid
    }

def grid_to_str(grid, size):
    lines = []

    for x in range(size):
        line = ""
        for y in range(size):
            line += "#" if grid[(x, y)] else " "
        lines.append(line)

    return "\n".join(lines)

from random import random
def generate_grid(size):
    return {
    (x, y): random() < 0.4
    for x in range(size)
    for y in range(size)
    }

def prepare_data(size):
    return [(0xff, 0xff, 0xff)] * (size * size)

def save_image(size, data):
    image = Image.new("RGB", (size, size))
    image.putdata(list(data))
    image.save("pycon.png")

increment = (0, -1, -1)
def paint_grid(grid, data, size):

    gen  = (grid[x, y] and increment or (0,0,0) for x in range(size) for y in range(size))
    return (tuple(map(lambda x: max(0, sum(x)), zip(a, b))) for a, b in zip(data, gen))


from tqdm import tqdm

if __name__ == "__main__":
    import time
    grid = generate_grid(300)
    data = prepare_data(300)
    for _ in tqdm(range(200)):
        data = paint_grid(grid, data, 300)
        grid = evolve(grid)
    save_image(300, data)
