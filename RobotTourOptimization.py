# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html


def calcul_distance(first_point_value, second_point_value):
    p0 = first_point_value
    p1 = second_point_value
    res = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    return res


def calcul_circuit(list_of_points, cycle):
    """
        Circuit length calculation
        Cycle: Order of the point in the alogorithm (name of the points)
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a float, a circuit length
    """

    return 0


def nearest_neighbor_algorithm(first_point, list_of_points):
    """
    Implement the nearest_neighbor algorithm.
    first_point: label of the first point
    list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
    return a list of point to visit, starting from first_point.
    """

    return list(list_of_points.keys())


def great_algorithm(first_point, list_of_points):
    """
        Implement a good algorithm to resolve the case.
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """

    return list(list_of_points.keys())


def optimal_algorithm(first_point, list_of_points):
    """
        Implement an optimal algorithm. This solution is the best, but it is slow
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """

    return list(list_of_points.keys())


def get_small_list_of_points():
    list_of_points = {
        0: (1, 3),
        1: (2, 5),
        2: (0, 6),
        3: (1, 7),
        4: (5, 1),
        5: (5, 5),
        6: (6, 3),
        7: (4, 4),
        8: (7, 0),
        9: (6, 6)
    }
    return list_of_points


def test_calcul_distance():
    a = (-3, -2)
    b = (5, 2)

    assert round(calcul_distance(a, b), 3) == 8.944


def test_calcul_min_circuit():
    a = (-3, -2)
    b = (5, 2)
    list_of_points = {'a': a, 'b': b}
    cycle = ['a', 'b']

    assert round(calcul_circuit(list_of_points, cycle), 3) == 17.889


def test_calcul_circuit():
    list_of_points = get_small_list_of_points()

    cycle = list(list_of_points.keys())
    distance = calcul_circuit(list_of_points, cycle)
    assert round(distance, 3) == 38.483


def test_return_sized():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point


def test_small_nearest_neighbor():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) <= 27


def test_big_nearest_neighbor():
    """I will test with a lot of points"""
    pass


def test_small_better_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_better_algorithm():
    """I will test with a lot of points"""
    pass


def test_small_optimal_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass
