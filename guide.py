"""
Problem: 10099 - The Tourist Guide
Author : Nicolas Ibagon Rivera
"""


from sys import stdin



def tarjan(G):
    global  depth, low,cont, parent1, time, child, art

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
    global time, bridges, cont, G
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

        elif parent1[u]!= v :
            low[u] = min(low[u], depth[v])
    return


def main():
    global G,art
    n = int(stdin.readline())
    case = 1
    while( n != 0):
        if(case != 1):
            print()

        cont = 0
        dicC = {}
        dicV = {}
        G = [[] for i in range(n)]

        for i in range(n):
            city = stdin.readline().strip()
            dicC[city] = cont
            dicV[cont] = city
            cont+=1
        r = int(stdin.readline())
        for i in range(r):
            cityR = stdin.readline().strip().split()

            G[dicC[cityR[0]]].append(dicC[cityR[1]])
            G[dicC[cityR[1]]].append(dicC[cityR[0]])
        tarjan(G)
        art = list(art)
        organize = []
        print('City map #{0}: {1} camera(s) found'.format(case,len(art)))
        for i in range(len(art)):
            organize.append(dicV[art[i]])
        case +=1
        organize.sort()
        for i in range(len(organize)):
            print(organize[i])
        n = int(stdin.readline())


main()
