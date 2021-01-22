"""
Problem: 13127 - Bank Robbery
Author : Nicolas Ibagon Rivera
"""



from sys import stdin
from heapq import heappush, heappop

global INF

INF = float('Inf')

def solve():
    global  G,  dist, visited, police, banks

    visited = [0 for i in range(len(G))]
    dist = [INF for i in range(len(G))]
    queue = []
    for i in range(len(police)):
        dist[police[i]] = 0
        heappush(queue,(0,police[i]))


    while (len(queue)):
        d,u = heappop(queue)
        if visited[u] == 0:
            visited[u] = 1
            for v,w in G[u]:
                duv = d + w
                if  dist[v] > duv:
                    dist[v] = duv
                    heappush(queue,(duv,v))


    max = -1
    for i in range(len(banks)):
        b = dist[banks[i]]
        if(max < b ):
            max = b
    cont = 0
    ans = []

    for i in range(len(banks)):
        if dist[banks[i]] == max:
                cont += 1
                ans.append(banks[i])

    ans.sort()
    if(isinstance(max,int)):
        print('{0} {1}'.format(cont,max))
        for i in range(len(ans)):
            if(i + 1 != len(ans)):
                print(ans[i], end =" ")
            else:
                print(ans[i], end ="")
        print()
    else:
        print('{0} *'.format(cont))
        for i in range(len(ans)):
            if(i + 1 != len(ans)):
                print(ans[i], end =" ")
            else:
                print(ans[i], end ="")
        print()

    return


def main():
    global G, dist, visited, police, banks
    s = stdin.readline().strip().split()
    while(len(s) == 4):
        s = list(map(int,s))
        m = s[1]
        G = [[] for i in range(s[0])]
        while(m > 0):

            tri = stdin.readline().strip().split()
            tri =  list(map(int,tri))
            G[tri[0]].append((tri[1],tri[2]))
            G[tri[1]].append((tri[0],tri[2]))
            m -=1

        banks = stdin.readline().strip().split()
        banks = list(map(int,banks))

        if s[3] != 0:
            police = stdin.readline().strip().split()
            police = list(map(int,police))
        else :
            police = []
        solve()

        s = stdin.readline().strip().split()
main()
