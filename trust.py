
"""
Problem: 11709 - Trust groups
Author : Nicolas Ibagon Rivera
"""


from sys import stdin

def dfs(u,num):
	global vis, scc
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)
	return

def dfs_list(u):
	global L, vis, I, G
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
	L.append(u)
	return


def compute():
	global L,I, scc, vis
	n = len(G)
	scc = [-1 for i in range(n)]

	I = [[] for i in range(n)]
	for i in range(n):
		for j in G[i]:
			I[j].append(i)
	vis = [0 for i in range(n)]
	L = []
	for i in range(n):
		if(vis[i] == 0):
			dfs_list(i)
	vis = [0 for i in range(n)]
	cont = 0
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont)
			cont +=	1
	return cont

def main():
    global G
    inp = stdin
    s = inp.readline().strip().split()
    s = list(map(int, s))

    while (s[0] != 0 or s[1] != 0):

        dic = {}
        cont = 0
        G = [[] for i in range((s[0]))]
        for i in range(int(s[0])):
            n = inp.readline().strip()

            dic[n] = cont
            cont += 1

        for i in range((s[1])):
            n1 = inp.readline().strip()
            n2 = inp.readline().strip()
            G[dic[n1]].append(dic[n2])

        print(compute())
        s = inp.readline().strip().split()
        s = list(map(int, s))

main()
