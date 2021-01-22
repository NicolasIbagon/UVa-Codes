
"""
Problem: 1193 - Radar Installation
Author : Nicolas Ibagon Rivera
"""

from sys import stdin
import math

def act_sch(a):
  #Tomado de camilorocha.info
  a.sort(key=lambda x : x[1])
  ans,n,N = 0,0,len(a)
  while n!=N:
    best,n,ans = n,n+1,ans+1
    while n!=N and a[n][0]<a[best][1]:
      n += 1
  return ans


def main():

    line = stdin.readline().split()
    cont = 1
    while line[0] != '0' and line[1] != '0':

        n,d = int(line[0]), int(line[1])
        arr = []
        confirm = False

        while n!=0:

            c = stdin.readline().split()
            x,y = int(c[0]), int(c[1])

            num = math.pow(d,2)-math.pow(y,2)

            if ( num < 0):
                confirm = True
            else:
                cateto = math.sqrt(num)
                arr.append((x-cateto, x+cateto))

            n-=1

        if(confirm):
            print('Case {0}: {1}'.format(cont,-1))
        else:
            print('Case {0}: {1}'.format(cont,act_sch(arr)))
        stdin.readline()
        line = stdin.readline().split()
        cont+=1
main()
