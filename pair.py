"""
Problem: 10245 - The Closest Pair Problem
Author : Nicolas Ibagon Rivera
"""

from sys import stdin

def solve(point):
  ans = 0.0
  for i in range(1,len(point)-1):
      d = sqrt(pow(point[i][0]-point[i-1][0],2)+pow(point[i][1]-point[i-1][1],2))
      if(ans  )
  return ans

def main():
  n = int(stdin.readline())
  while n!=0:
    point = list()
    for _ in range(n):
      tok = stdin.readline().split()
      point.append((float(tok[0]), float(tok[1])))
    print('{0:.4f}'.format(solve(point)))
    n = int(stdin.readline())

main()
