import pyconcz

def test_get_alive_neighbors():
    grid = {
     (x, y): True
     for x in range(10)
     for y in range(10)
    }

    assert 3 == pyconcz.get_alive_neighbors(grid, (0, 0))
    assert 8 == pyconcz.get_alive_neighbors(grid, (1, 1))

def test_get_neighbours():
    expected = {
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2),
    }

    assert expected == set(pyconcz.get_neighbours((1, 1)))

def test_overcrowded_cell_should_die():
    grid = {
     (x, y): True
     for x in range(10)
     for y in range(10)
    }

    assert not pyconcz.should_live(grid, (1, 1))

def test_overcrowded_cell_should_die():
    grid = {
     (x, y): True
     for x in range(10)
     for y in range(10)
    }

    new_grid = {
     (x, y): False
     for x in range(10)
     for y in range(10)
    }
    new_grid[(0, 0)] = new_grid[(9, 0)] = new_grid[(0, 9)] = new_grid[(9, 9)] = True

    assert new_grid == pyconcz.evolve(grid)

def test_print_grid():
    grid = {
       (0, 0): True,
       (0, 1): False,
       (1, 0): False,
       (1, 1): True,
    }

    assert '# \n #' == pyconcz.grid_to_str(grid, 2)
