#!/usr/bin/env python3

class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]


import sys

def main():

    with open('graph01.txt') as f:

        V = int(f.readline())

        g = Graph(V)

        for line in f:

            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    paths = DFSPaths(g, 0)

    print(paths.hasPathTo(6))
    print(paths.pathTo(6))

if __name__ == '__main__':
    main()
