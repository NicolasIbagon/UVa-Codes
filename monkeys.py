"""
Problem: 776 - Monkeys in a Regular Forest
Author : Nicolas Ibagon Rivera
"""



from sys import stdin
from collections  import deque

def form(n):





    return ans


def dfs(i, j):
    global M, ans, cont,f,col
    qi = deque()
    qi.append(i)
    qj= deque()
    qj.append(j)
    dr=[-1,1,0,0,-1,-1,1,1]
    dc=[0,0,1,-1,-1,1,-1,1]
    ans[i][j] = cont
    while(len(qi) and len(qj)):
        i = qi.pop()
        j = qj.pop()
        for k in range(len(dr)):
             rr = i + dr[k]
             cc = j + dc[k]
             if rr < 0 or cc < 0 : continue
             elif rr >= col or cc >= f : continue
             else :
                 if M[i][j] == M[rr][cc] and ans[rr][cc] == 0 :
                    ans[rr][cc] = cont
                    qi.append(i+ dr[k])
                    qj.append(j + dc[k])
    return


def solve():
  global ans, cont,f, col, M
  f = len(M[0])
  ans = [[0 for i in range(f)] for j in range(col)]
  cont = 0
  for i in range(col):
      for j in range(f):

        if ans[i][j] == 0:
            cont +=1
            dfs(i, j)

  return



def main():
  global ans, cont,f, col, M, cont

  inp = stdin
  s = inp.readline().strip().split()
  M =[]
  col = 0
  while( len(s) != 0 ):
        if(s[0] == '%'):
            solve()
            for i in range(len(ans)):
                ans[i] = list(map(str,ans[i]))
            tamaño = []
            for j in range(len(ans[0])):
                maxim = 0
                for i in range(len(ans)):
                    if maxim <len( ans[i][j]):
                        maxim = len(ans[i][j])
                tamaño.append(maxim)
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    if(j != 0):
                        print( ''.join(ans[i][j].rjust(tamaño[j]+1)), end= "")
                    else:
                        print( ''.join(ans[i][j].rjust(tamaño[j])), end= "")
                print()
            print("%")
            col = 0
            M =[]

        else:
            M.append(s)
            col +=1
        s = inp.readline().strip().split()

  solve()
  for i in range(len(ans)):
      ans[i] = list(map(str,ans[i]))


  tamaño = []
  for j in range(len(ans[0])):
      maxim = 0
      for i in range(len(ans)):
          if maxim <len( ans[i][j]):
              maxim = len(ans[i][j])
      tamaño.append(maxim)

  for i in range(len(ans)):
      for j in range(len(ans[i])):

          if(j != 0):

              print( ''.join(ans[i][j].rjust(tamaño[j]+1)), end= "")

          else:
              print( ''.join(ans[i][j].rjust(tamaño[j])), end= "")
      print()
  print("%")




main()
