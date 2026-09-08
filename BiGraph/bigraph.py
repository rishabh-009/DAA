import BiGraph.dynamicintarray as dia
import numpy as np


class BiGraph:
    root = None
    V = None
    E = None

    def __init__(self, path):
        f = open(path)
        self.V = int(f.readline())
        self.E = int(f.readline())
        self.root = np.empty(self.V, dtype='object')
        for i in range(self.V):
            self.root[i] = dia.DynamicIntArray(0)
        for i in range(self.E):
            line = f.readline().strip()
            if not line:
                break
            p,q = map(int, line.split())
            self.addEdge(p, q)
        f.close()
    def addEdge(self, p, q):
        self.root[p].insert(q)
        self.root[q].insert(p)
    def get_V(self):
        return self.V
    def get_E(self):
        return self.E
    def adj(self, p):
        return self.root[p]
    def toString(self):
        for v in range(self.V):
            darr = self.adj(v)
            for w in darr:
                print(str(v) + " - " + str(w))



class depthfirstsearch():
    g = None
    source = None
    visited = None
    edgeTo = None

    def __init__(self, graph, s):
        self.g = graph
        self.source = s
        self.visited = np.zeros(self.g.get_V(), dtype=bool)
        self.edgeTo = np.full(self.g.get_V(), -1, dtype=int)
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for neighbor in self.g.adj(v):
            if not self.visited[neighbor]:
                self.edgeTo[neighbor] = v
                self.dfs(neighbor)

    












        




g = BiGraph("D:\\Learning\\DAA/tinyG.txt")
path = depthfirstsearch(g, 0)
g.toString()