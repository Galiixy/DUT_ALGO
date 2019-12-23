import math
import copy
import numpy as np
import itertools


def calcul_distance(first_point_value, second_point_value):
    p0 = first_point_value
    p1 = second_point_value
    res = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    return res


def calcul_circuit(list_of_points, cycle):
    distance = 0
    i = 0
    for i in range(len(cycle)):
        coordP1 = list_of_points[cycle[i]]
        if(i == (len(cycle)-1)):
            coordP2 = list_of_points[cycle[0]]
            distance += calcul_distance(coordP1, coordP2)
        else:
            coordP2 = list_of_points[cycle[i+1]]
            distance += calcul_distance(coordP1, coordP2)
    return distance


def fusion(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    n = n1+n2
    j = 1
    k = 1
    tab = [0]*(n)
    for i in range(n):
        if((j <= n1) and ((k > n2) or (tab1[j-1][1] <= tab2[k-1][1]))):
            tab[i] = tab1[j-1]
            j = j+1
        else:
            tab[i] = tab2[k-1]
            k = k+1
    return tab


def merge_sort(tab):
    longueurtab = len(tab)
    n1 = round(longueurtab/2)
    n2 = longueurtab-n1
    if(longueurtab == 1):
        return tab
    else:
        tab1 = [0]*(n1)
        tab2 = [0]*(n2)
        for i in range(n1):
            tab1[i] = tab[i]
        for j in range(n2):
            tab2[j] = tab[n1+j]
        tab1 = merge_sort(tab1)
        tab2 = merge_sort(tab2)
        tab = fusion(tab1, tab2)
    return tab


def nearest_neighbor_algorithm(first_point, list_of_points):
    p0 = list_of_points[first_point]
    unvisited = copy.copy(list_of_points)
    del unvisited[first_point]
    visited = list()
    visited.append(first_point)
    p = p0
    while len(unvisited) != 0:
        res = [0]*(len(unvisited))
        i = 0
        for point in unvisited:
            distance = calcul_distance(p, unvisited[point])
            res[i] = (point, distance, unvisited[point])
            i = i+1
        res = MergeSort(res)
        p = res[0]
        visited.append(p[0])
        del unvisited[p[0]]
    return list(visited)


def get_Matrice(first_point, list_of_points, matrice_dist, long):
    matrice_point = [0]*(long)
    point_ref = list_of_points[first_point]
    points = copy.copy(list_of_points)
    del points[first_point]
    matrice_dist[0][0] = first_point
    for cpt_ligne in range(long):
        matrice_point[0] = list_of_points[cpt_ligne]
        matrice_dist[cpt_ligne][0] = cpt_ligne
        cpt_colonne = 1
        for index_point in points:
            distance = calcul_distance(point_ref, points[index_point])
            matrice_dist[cpt_ligne][cpt_colonne] = distance
            matrice_point[cpt_colonne] = points[index_point]
            cpt_colonne = cpt_colonne + 1
        points[long+cpt_ligne] = point_ref
        point_ref = matrice_point[1]
        del points[cpt_ligne+1]
    return matrice_dist


def great_algorithm(first_point, list_of_points):
    long = len(list_of_points)
    matrice_dist = np.zeros((long, long))
    distance_min = 100000
    distance_max = 0
    points = list()
    matrice_dist = get_Matrice(first_point, list_of_points, matrice_dist, long)
    for cpt_col in range(1, long):
        if(matrice_dist[first_point][cpt_col] > distance_max):
            cpt_point = first_point + cpt_col
            if(cpt_point >= long):
                    cpt_point = cpt_point-long
            distance_max = matrice_dist[first_point][cpt_col]
    points.append(first_point)
    points.append(cpt_point)
    while(len(points) != long):
        distance_min = 100000
        index_min = 0
        for cpt_col in range(1, long):
            distance = matrice_dist[cpt_point][cpt_col]
            index_min = cpt_point + cpt_col
            if(index_min >= long):
                    index_min = index_min - long
            if(len(points) == (long-1) and index_min not in points):
                index_point = index_min
            if(distance <= distance_min and index_min not in points):
                distance_min = distance
                index_point = index_min
        points.append(index_point)
        cpt_point = index_point
    return list(points)


def optimal_algorithm(first_point, list_of_points):
    distance_circuit = 10000
    circuit = copy.copy(list_of_points)
    del circuit[first_point]
    permutations = list(itertools.permutations(circuit))
    for circuit_permute in permutations:
        circuit_permute = (first_point,) + circuit_permute
        if(calcul_circuit(list_of_points, circuit_permute) < distance_circuit):
            distance_circuit = calcul_circuit(list_of_points, circuit_permute)
            circuitOptimal = circuit_permute
    return list(circuitOptimal)


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


def get_tricky_points():
    list_of_points = {
        0: (0, 0),
        1: (0, 1),
        2: (0, 3),
        3: (0, 11),
        4: (0, -21),
        5: (0, -5),
        6: (0, -1),
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
    circuit_cost = calcul_circuit(list_of_points, result)
    assert round(circuit_cost) <= 27
    assert round(circuit_cost, 2) == 24.75
    assert result == [0, 2, 3, 1, 7, 5, 9, 6, 8, 4]


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass


def test_tricky_nearest_neighbor():
    list_of_points = get_tricky_points()
    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) <= 80


def test_tricky_better_algorithm():
    list_of_points = get_tricky_points()
    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) < 80


def test_tricky_optimal_algorithm():
    list_of_points = get_tricky_points()
    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) == 64