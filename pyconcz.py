def cell_alive(current, live_neighbors):

    # Live with < 2 : die
    if current and live_neighbors < 2:
        return False

    # Live with 2 or 3 : live
    if current and live_neighbors in (2, 3):
        return True

    # Dead with == 3 : live
    if not current and live_neighbors == 3:
        return True

    # Live with > 3 : die
    if current and live_neighbors > 3:
        return False


def get_neighbors(coords):
    x, y = coords
    return {
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),         (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1),
    }

def alive_neighbors(coords, grid):
    neighbors = get_neighbors(coords)
    return sum(n in grid for n in neighbors)

def grid_to_str(grid, size):
    lines = []
    for y in range(size):
        line = []
        for x in range(size):
            if (x, y) in grid:
                line.append('#')
            else:
                line.append(' ')
        lines.append(''.join(line))
    return '\n'.join(lines)

def step(grid, size):
    return {
        (x, y)
        for x in range(size)
        for y in range(size)
        if cell_alive((x, y) in grid, alive_neighbors((x, y), grid))
    }

