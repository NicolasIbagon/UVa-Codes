
"""
Problem: 315 - Network
Author : Nicolas Ibagon Rivera
"""


from sys import stdin


def tarjan():
    global G, depth, low,cont, parent1, time, child, art

    time = 0
    n = len(G)
    art = set()
    parent1 = [-1 for i in range(n)]
    depth = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    for u in range(n):
        if depth[u] == -1:
            dfs(u)
    return

def dfs(u):
    global time
    depth[u] =  time
    low[u] = depth[u]
    time +=1
    child = 0
    for v in G[u]:
        if depth[v] ==-1:       
            parent1[v] = u
            child += 1
            dfs(v)
            low[u] = min(low[u], low[v])
            if (parent1[u] == -1 and child > 1) or (low[v] >= depth[u] and parent1[u] != -1):
                art.add(u)

        elif depth[v] < depth[u] - 1 :
            low[u] = min(low[u], depth[v])
    return

def solve():
    global G
    tarjan()
    print(len(art))




def main():
     global G,s
     s = int(stdin.readline())
     while s!=0:
         G = [ set() for _ in range(s) ]
         n = stdin.readline().split()
         lista = []
         for i in range(len(n)):
             lista.append(int(n[i]))
         while lista[0]!=0:
             for i in range(1, len(lista)):
                 G[lista[0]-1].add(lista[i]-1)
                 G[lista[i]-1].add(lista[0]-1)
             n = stdin.readline().split()
             lista = []
             for i in range(len(n)):
                 lista.append(int(n[i]))
         solve()
         s = int(stdin.readline())

main()
