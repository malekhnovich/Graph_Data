import abc
import numpy as np

class Graph(abc.ABC):

    def __init__(self,numVertices,directed = False):
        self.numVertices = numVertices
        self.directed = directed

    #abc.abstractmethod
    def add_edge(self,v1,v2,weight):
        pass

    #abc.abstractmrthod
    def get_adjacent_vertices(self,v):
        pass

    #abc.abstractmethod
    def get_indegree(self,v):
        pass

    #abc.abstractmethod
    def get_edge_weight(self,v1,v2):
        pass

    #abc.abstract method
    def display(self):
        pass

class AdjacencyMatrixGraph(Graph):

    def __init__(self,numVertices,directed = False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices,directed)

        self.matrix = np.zeros((numVertices,numVertices))

    def add_edge(self,v1,v2,weight=1):
        if v1 >= self.numVertices or v2>=self.numVertices or v1 < 0  or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds"%(v1,v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight
