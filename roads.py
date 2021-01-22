"""
Problem: 10308 - Roads in the North
Author : Nicolas Ibagon Rivera
"""




from sys import stdin
from collections import deque

def bfs(u):
    global tree, dis, max
    q = deque()
    q.append(u)
    dis[u] = 0
    while(len(q)):
        v = q.popleft()
        for w in tree[v]:
            if(dis[w[0]] == -1):
                q.append(w[0])
                dis[w[0]] = dis[v] + w[1]
    print(dis)
    max = -99
    for u in tree:
        if max < dis[u]:
            max = dis[u]
    return

def solve():
    global tree, dis, max
    dis = { u : -1 for u in tree }

    for u in tree:

        if dis[u] == -1:
            bfs(u)
    print(max)
    return


def main():
    global tree, dis, max
    s = stdin.readline().strip().split()
    s = list(map(int,s))
    while(len(s) > 0):
        tree = {}
        while(len(s) > 0):
            if s[0] not in tree:
                tree[s[0]] = [(s[1],s[2])]

            else:
                tree[s[0]].append((s[1],s[2]))
            if s[1] not in tree:
                tree[s[1]] = [(s[0],s[2])]
            else:
                tree[s[1]].append((s[0],s[2]))
            s = stdin.readline().strip().split()
            s = list(map(int,s))
        solve()
        s = stdin.readline().strip().split()
        s = list(map(int,s))




main()
