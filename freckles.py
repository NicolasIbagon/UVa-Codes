"""
Problem: 10034 - Freckles
Author : Nicolas Ibagon Rivera
"""

import math
from sys import stdin

#Codigo algoritmo Kruskal tomado de 2018-2 agra Camilo Rocha

class dforest(object):
  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
  
  def find(self, x):
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
      else:
        self.__parent[fx] = fy
        if rx==ry:
          self.__rank[fy] += 1

def kruskal(graph, lenv):
  ans = list()
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0

  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans.append((u,v,d))

      df.union(u, v)

    i += 1

  return ans



def main():

    s = int(stdin.readline())
    while( s > 0):
        n = stdin.readline().strip()
        if(len(n) > 0):
            n = int(n)
            freckles = n
            graph = []
            listCor = []
            n-=1
            cor = stdin.readline().strip().split()
            cor = list(map(float, cor))
            listCor.append(cor)

            while(n > 0):
                cor = stdin.readline().strip().split()
                cor = list(map(float, cor))
                listCor.append(cor)
                n-=1







            for i in range(freckles):
                for j in range(i+1,freckles):

                    d = math.sqrt(((listCor[i][0]-listCor[j][0])**2)+((listCor[i][1]-listCor[j][1])**2) )

                    graph.append((i,j,d))

            graph = kruskal(graph,freckles)
            sum = 0
            for i in range(len(graph)):
                sum+= graph[i][2]


            print('{0:.2f}'.format(sum))




            if(s > 1): print()
            s -=1

main()
