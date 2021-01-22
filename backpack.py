"""
Problem: 907 - Winterim Backpacking Trip
Author : Nicolas Ibagon Rivera
"""
from sys import stdin



def tripS(dist, mid, n, k):
    suma,i = 0,0
    l = len(dist)
    while n!=0 and k >= 0 and l  > i:
        suma = dist[i]+ suma
        if( suma > mid):
            suma = 0
            k = k - 1
        else:
            n = n - 1
            i+=1
    return k >=0




def binary(dist, low, hi, n, k, maxim):

    if hi!= 0:
        while low+1 != hi:
            mid = low + ((hi-low)>>1)
            if mid >= maxim:
                if tripS(dist, mid, n, k):
                    hi = mid
                else: low = mid
            else:
                low = mid
    return hi



def solve(n, k, dist):
  ans = None

  maxim = -1
  suma = 0
  for i in range(len(dist)):
      suma = dist[i] + suma
      if(maxim < dist[i] ): maxim = dist[i]

  ans = binary(dist, 0, suma, n+1, k, maxim)

  return ans

def main():
  N,K,dist = None,None,None
  line = stdin.readline()
  while len(line)!=0:
    N,K = map(int, line.split())
    dist = [ int(stdin.readline()) for _ in range(N+1) ]
    print(solve(N, K, dist))
    line = stdin.readline()

main()
