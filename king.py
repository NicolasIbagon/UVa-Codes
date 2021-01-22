"""
Problem: 11352 - Crazy King
Author : Nicolas Ibagon Rivera
"""


from sys import stdin
from collections import deque



def bfs(mat,a,b,matriz,n,m):
	dist=[[9999 for i in range(m)] for j in range(n)]
	qi=deque()
	qi.append(a[0])
	qj=deque()
	qj.append(a[1])
	dr=[-1,1,0,0,-1,-1,1,1]
	dc=[0,0,1,-1,-1,1,-1,1]
	mat[a[0]][a[1]] = 1
	dist[a[0]][a[1]]=0
	while(len(qi) and len(qj)):
		i = qi.popleft()
		j = qj.popleft()
		if matriz[i][j] == 'B':
			return dist[b[0]][b[1]]
		for k in range(len(dr)):
			rr = i + dr[k]
			cc = j + dc[k]
			if rr < 0 or cc < 0 : continue
			elif rr >= n or cc >= m : continue
			else:
				if mat[rr][cc] == 0:
					mat[rr][cc] = 1
					if(dist[rr][cc] > dist[i][j] + 1):
						dist[rr][cc] = dist[i][j] + 1
					qi.append(rr)
					qj.append(cc)

	return -1

def solve(matriz,n,m):

	horsei =[-1,-2,-2,-1,+1,+2,+1,+2]
	horsej =[-2,-1,+1,+2,-2,-1,+2,+1]

	mat = [[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		for j in range(m):
			if(matriz[i][j] == 'A'):
				a = (i,j)
			elif(matriz[i][j] == 'B'):

				b = (i,j)
			elif(matriz[i][j] == 'Z'):
				mat[i][j] = 1
				for k in range(len(horsei)):
					hi = i + horsei[k]
					hj = j + horsej[k]

					if hi < 0 or hj < 0 : continue
					elif hi >= n or hj >= m : continue
					else:
						if matriz[hi][hj] == '.':
							mat[hi][hj] = 1

	ans = bfs(mat,a,b,matriz,n,m)
	if ans == -1:
		print("King Peter, you can't go now!")
	else:
		print("Minimal possible length of a trip is {0}".format(ans))

	return



def main():
	inp = stdin
	s=int(inp.readline())
	while( s > 0):
		n  = inp.readline().strip().split()

		M = []
		for i in range(int(n[0])):
			k  = inp.readline().strip("\n")
			M.append(k)

		solve(M,int(n[0]),int(n[1]))

		s -= 1

	return
main()
