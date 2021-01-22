
"""
Problem: 200 - Rare Order
Author : Nicolas Ibagon Rivera
"""



from sys import stdin
from collections import deque

def topoSort(G):
    n = len(G)
    indeg = { u : 0 for u in G }
    for u in G:
        for v in G[u]:

            if v not in indeg:
                indeg[v] = 0
            if indeg[v] == 0:
                    indeg[v] = 1
            else:
                indeg[v] = 1 + indeg[v]
    topo = []
    indeg0 = deque()                
    for u in indeg:

        if indeg[u] == 0:
            indeg0.appendleft(u)

    while len(topo) < n:
        i = indeg0.pop()
        topo.append(i)
        for j in G[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                indeg0.appendleft(j)
    return topo

def makeGraph(array, letters):
    for i in range(1, len(array)):
        mini = min(len(array[i]), len(array[i-1]))
        j = 0
        while( j < mini):
            if(array[i][j] != array[i-1][j]):
                    if array[i-1][j] not in letters:
                            letters[array[i-1][j]] = []
                    if array[i][j] not in letters:
                            letters[array[i][j]] = []
                    letters[array[i-1][j]].append(array[i][j])
                    j = mini
            j +=1
    return

def solve(array):
    global letters
    letters = {}

    makeGraph(array, letters)
    return

def main():
    global letters
    inp = stdin
    s = inp.readline().strip("\n")
    array = []

    while len(s) > 0:

            if(s[0] == '#' ):
                solve(array)

                if not  bool(letters):
                    print(''.join(array))
                else:


                    print(''.join(topoSort(letters)))
                array = []

            else:
                array.append(s)

            s = inp.readline().strip("\n")



main()
