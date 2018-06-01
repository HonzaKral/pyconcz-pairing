import pyconcz

def test_add():
    neighbors_of_1_1 = set([
       (0,0), (1,0), (2,0),
       (0,1),        (2,1),
       (0,2), (1,2), (2,2)])

    g = pyconcz.Grid()

    for i in neighbors_of_1_1:
        g.cells[i] = True

    g.cells[(1,1)] = True


    assert g.neighbour_cells( (1, 1) ) == 8

    assert not g.alive_or_dead( (1, 1) )
    assert g.alive_or_dead( (0, 0) )
