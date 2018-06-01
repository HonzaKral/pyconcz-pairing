import pyconcz


def test_get_all_neighbors():
    start = (1, 1)
    expected = {
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2),
    }

    assert expected == set(pyconcz.get_neighbors(start))


def test_alive_neighbors():
    grid = {(0, 0), (1, 0)}

    assert 2 == pyconcz.alive_neighbors((1, 1), grid)

def test_cell_alive():
    assert not pyconcz.cell_alive(True, 1)
    assert pyconcz.cell_alive(True, 2)
    assert pyconcz.cell_alive(True, 3)
    assert not pyconcz.cell_alive(True, 4)

    assert not pyconcz.cell_alive(False, 2)
    assert pyconcz.cell_alive(False, 3)
    assert not pyconcz.cell_alive(False, 4)

def test_grid_to_str():
    assert " # \n#  \n   " == pyconcz.grid_to_str({
        (0, 1), (1, 0)
        }, 3)

def test_step():
    grid = set()
    for x in range(10):
        for y in range(10):
            grid.add((x, y))

    assert {(0, 0), (9, 0), (0, 9), (9, 9)} == pyconcz.step(grid, 10)

