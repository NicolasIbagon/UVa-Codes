"""
Problem: 1112 - Mice and Maze
Author : Nicolas Ibagon Rivera
"""


from sys import stdin
from heapq import heappush, heappop

global INF

INF = float('inf')
def solve():
    global e,  G,  dist, visited, n, t

    visited = [0 for i in range(len(G))]
    dist = [INF for i in range(len(G))]
    dist[e] = 0
    queue = [(0, e)]

    while (len(queue)):
        d,u = heappop(queue)
        if visited[u] == 0:
            visited[u] = 1
            for v,w in G[u]:
                duv = d + w
                if  dist[v] > duv:
                    dist[v] = duv
                    heappush(queue,(duv,v))

    ratones = 0
    for i in range(len(G)):
        if(dist[i] <= t):
            ratones += 1

    return ratones





def main():
    global e, dist, visited, n, G, t
    s = int(stdin.readline())
    while( s >0 ):
        n = stdin.readline().strip()
        if( len(n) > 0):
            n = int(n)
            e = int(stdin.readline())-1
            t = int(stdin.readline())
            m = int(stdin.readline())
            G = [[] for i in range(n)]

            while(m > 0):
                line = stdin.readline().strip().split()
                line = list(map(int,line))

                G[line[1]-1].append((line[0]-1,line[2]))
                m -= 1

            print(solve())

            if(s > 1): print()

            s -= 1
main()
