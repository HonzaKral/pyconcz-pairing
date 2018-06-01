import pyconcz

def test_neighbors_finds_all_neighbors():
    start = (1, 1)
    expected = {
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2),
    }

    assert expected == set(pyconcz.get_neighbors(start))

def test_neighbors_finds_all_neighbors_in_corner():
    start = (0, 0)
    expected = {
                (0, 1),
        (1, 0), (1, 1),
    }

    assert expected == set(pyconcz.get_neighbors(start))

def test_neighbors_finds_all_neighbors_in_lower_corner():
    start = (9, 9)
    expected = {
        (8, 8), (8, 9),
        (9, 8),
    }

    assert expected == set(pyconcz.get_neighbors(start))

def test_live_neighbors():
    grid = [
        [True for _ in range(10)] for _ in range(10)
    ]

    assert 3 == pyconcz.alive_neighbors(grid, (0, 0))



def test_overcrowded_cell_dies():
    grid = [
        [True for _ in range(10)] for _ in range(10)
    ]

    assert not pyconcz.should_live(grid, (1, 1))


def test_array_to_string():
    grid = [
        [True, False, False],
        [True, True,  False],
        [True, False, True],
    ]

    output = "#  \n## \n# #"
    assert pyconcz.grid_to_string(grid)


