# https://docs.python.org/3/library/itertools.html#itertools.combinations
# https://www.tutorialspoint.com/how-do-i-customize-the-display-of-edge-labels-using-networkx-in-matplotlib


import matplotlib.pylab as plt
import networkx as nx
from itertools import combinations


def solvemaze(lst):
    # make sure valid input
    try:
        V = lst[0]
        maze = lst[1]
        AddEdge = lst[2]
        k = lst[3]
        vs = lst[4]
        vt = lst[5]

        # initialize graph G
        G = nx.Graph()
        G.add_nodes_from(V)
        G.add_edges_from(maze)
        distance = len(nx.shortest_path(G, (0, 3), (3, 0))) - 1
        permutations = combinations(AddEdge, k)

        # naive solution - pass on all the permutation
        for i in permutations:
            G.add_edges_from(i)
            if len(nx.shortest_path(G, (0, 3), (3, 0))) - 1 < distance:
                distance = len(nx.shortest_path(G, (0, 3), (3, 0))) - 1
            G.remove_edges_from(i)
    except:
        print("The input is not correct")

    return(distance)


# run example
if __name__ == '__main__':
    maze = {((2, 1), (3, 1)), ((2, 0), (3, 0)), ((1, 0), (1, 1)), ((3, 0), (3, 1)), ((1, 3), (2, 3)), ((0, 2), (0,
            3)), ((0, 2), (1, 2)), ((1, 1), (1, 2)), ((2, 2), (3, 2)), ((2, 2), (2, 3)), ((3, 1), (3, 2)), ((1, 2), (1, 3)),
            ((2, 3), (3, 3)), ((0, 0), (1, 0)), ((0, 1), (1, 1))}
    AddEdge = {((0, 0), (0, 1)), ((0, 3), (1, 3)), ((0, 1), (0, 2)), ((2, 0), (2, 1)), ((1, 0), (2, 0)), ((1, 1),
                (2, 1)), ((3, 2), (3, 3)), ((2, 1), (2, 2)), ((1, 2), (2, 2))}
    V = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}
    k = 1
    vt = (3, 0)
    vs = (0, 3)
    lis = [V, maze, AddEdge, k, vs, vt]
    solvemaze(lis)

