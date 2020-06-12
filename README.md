# Projet Robot
## Description
Projet DUT Informatique d'Algorithmie 
## Features
### Algo 1 - nearest
```markdown
def nearest_neighbor_algorithm(first_point, list_of_points):
```
- first_point: label of the first point
- list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
- return a list of point to visit, starting from first_point

Goal :
Implement the nearest_neighbor algorithm. Get the closest points. 

Process :
    1. On recupere la liste des distance tel que : res[i] = (point en question, distance par rapport a p)
    2. On fait un tri sur cette liste pour connaître le plus proche

#### merge_sort


### Algo 2 - better
```markdown
def great_algorithm(first_point, list_of_points):
```
- first_point: label of the first point
- list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
- return a list of point to visit, starting from first_point

Goal :
Implement a good algorithm to resolve the case. Better than algo 1 but the solution is less good than algo 3.

Process :
    1. Récupérer la matrice distance de la forme : index, distancepointsuivant1, distancepointsuivant2
    2. On part du point de départ on va jusqu'au point le plus éloigné avec ce point , puis on fait au plus proche  

#### get_matrice_dist


### Algo 3 - optimal
```markdown
def optimal_algorithm(first_point, list_of_points):
```
- first_point: label of the first point
- list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
- return a list of point to visit, starting from first_point

Goal :
Implement an optimal algorithm. This solution is the best, but it is slow.
 
Process :
    1. On copie la liste de points
    2. On retire le premier point de la permutation
    3. On calcul de toutes les possibilites de circuit
    4. On remet le premier point au circuit

## Installation 

## Code Style

## Contact
If you need more informations you can contact us : Gaelle FERREIRA : gaelle.ferreira.77@gmail.com , Julien Dewerpe : 
