# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html
import copy

def calcul_distance(first_point_value, second_point_value):
    p0 = first_point_value
    p1 = second_point_value
    res = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    return res

#fonctions utiles --------------------------------------------------------
 #tri naïf
def Fusion(tab1,tab2):
    n1=len(tab1) 
    n2= len(tab2)
    n= n1+n2
    j=1
    k=1
    tab=[0]*(n)
    
    for i in range(n):
        if((j<=n1) and ((k>n2) or (tab1[j-1][1]<=tab2[k-1][1]))):
          tab[i] = tab1[j-1]
          j=j+1
        else:
            tab[i]=tab2[k-1]
            k=k+1
    return tab

def MergeSort(tab):
    'declaration'
    longueurtab = len(tab)
    n1 = round(longueurtab/2)
    n2 = longueurtab-n1
    
    if (longueurtab==1):
        return tab
    else:
        'declarations'
        tab1=[0]*(n1)
        tab2=[0]*(n2)

        'traitement'
        for i in range(n1):
            tab1[i] =tab[i]
            
        for j in range(n2):
            tab2[j]=tab[n1+j]
            
        tab1 = MergeSort(tab1)
        tab2 = MergeSort(tab2)
        
        tab = Fusion(tab1, tab2)
    return tab

 #tri efficace (Quick sort)
def pivot(tab,cpt_debut,cpt_fin): 
    index = cpt_debut-1
    pivot = tab[cpt_fin] 
    value=0
    for i in range(cpt_fin , cpt_debut):
        if   tab[i] <= pivot:       
            index = index+1 
            value = tab[i]
            tab[i]= tab[index]
            tab[index]=value
    value= tab[index+1]
    tab[index+1]=tab[cpt_fin]
    tab[cpt_fin] = tab[index+1] 
    return (index+1) 
  
# Function to do Quick sort 
def quickSort(tab,cpt_debut,cpt_fin): 
    if (cpt_debut < cpt_fin): 
        v_pivot = pivot(tab,cpt_debut,cpt_fin)
        quickSort(tab,cpt_debut,v_pivot-1) 
        quickSort(tab,v_pivot+1+1,cpt_fin)

def calcul_circuit(list_of_points, cycle):
    """
        Circuit length calculation
        Cycle: Order of the point in the alogorithm (name of the points)
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a float, a circuit length
    """
    distance = 0
    i = 0
    for i in range (len(cycle)):
        "si i est a la derniere case de cycle"
        if (i == (len(cycle) - 1)):
            distance +=calcul_distance(list_of_points[cycle[i]], list_of_points[cycle[0]])
        else:
            distance +=calcul_distance(list_of_points[cycle[i]], list_of_points[cycle[i + 1]])
        return distance


def nearest_neighbor_algorithm(first_point, list_of_points):
    """
    Implement the nearest_neighbor algorithm.
    first_point: label of the first point
    list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
    return a list of point to visit, starting from first_point.

    prendre un point initial p0 de la liste
    p = p0
    i = 0
    tant qu'il y a encore des points non-visités
    i = i + 1
    on prend 
    """

    p0 = list_of_points[first_point]
    unvisited = copy.copy(list_of_points)
    del unvisited[first_point]
    visited = list()
    visited.append(first_point)
    p = p0
    while len(unvisited) != 0 :
        res = [0]*(len(unvisited))
        i = 0
        for point in unvisited:
            "on recupere la liste des distance "
            "res[i] = (point en question, distance par rapport a p)"
            res[i] = (point,  calcul_distance(p, unvisited[point]),unvisited[point])
            i=i+1
        "tri sur le tuple les distance"
        res = MergeSort(res)
        p = res[0]
        visited.append(p[0])
        del unvisited[p[0]]
    return list(visited)





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

test_small_nearest_neighbor()