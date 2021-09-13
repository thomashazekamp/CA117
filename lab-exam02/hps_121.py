#!/usr/bin/env python3

class Graph(object):

  def __init__(self, V):
    self.V = V
    self.adj = {}
    for v in range(V):
      self.adj[V] = list()

  def addEdge(self, v, w):
    self.adj[v].append(w)
    self.adj[w].append(v)

