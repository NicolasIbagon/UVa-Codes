"""
Problem: 11747 - Heavy Cycle Edges
Author : Nicolas Ibagon Rivera
"""


from sys import stdin

#Codigo algoritmo Kruskal tomado de 2018-2 agra Camilo Rocha

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the numnber of components"""
    return self.__ccount

  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1
      self.__ccount -= 1

def kruskal(graph, lenv):
  ans = list()
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0

  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u) == df.find(v):
      ans.append((d))
    else:
      df.union(u, v)

    i += 1


  return ans










def main():


    s = stdin.readline().strip().split()
    s = list(map(int,s))

    while(s[0] != 0 or s[1] != 0):
        e = s[1]
        graph = []

        while( e > 0):
            edge = stdin.readline().strip().split()
            edge = list(map(int, edge))
            graph.append((edge[0],edge[1],edge[2]))
            e-=1

        ans = kruskal(graph, s[0])
        if(len(ans) == 0):

            print('forest')

        else:

            for i in range(len(ans)):
                if(i+1 != len(ans)): print( ans[i] ,end=" ")
                else: print( ans[i] ,end="")
            print()

        s = stdin.readline().strip().split()
        s = list(map(int,s))






main()
