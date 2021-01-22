"""
Problem: 10474 - Where is the Marble?
Author : Nicolas Ibagon Rivera
"""

from sys import stdin

marble,lenm = None,None


def binary(marble,low,hi,x):
	if hi!= 0:
		while low+1!=hi:
			mid = low + ((hi-low)>>1)
			if x < marble[mid]: hi = mid
			else: low = mid
		ans = low
	return ans

def solve(x):
  global marble,lenm
  ans =  binary(marble,0,lenm, x)

  while(marble[ans-1] == marble[ans]):
      ans = ans-1


  return ans

def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]

  while lenm+lenq!=0:
    marble = []
    i = 0
    while i < lenm:
        inpu = inp.readline().strip()
        if len(inpu) != 0:
           marble.append(int(inpu))
           i+=1
    marble.sort()
    print('CASE# {0}:'.format(cas))
    q = 0
    while q < lenq:
        x = inp.readline().strip()
        if len(x) != 0:
            q+=1
            ans = solve(int(x))
            if ans==-1 or marble[ans]!=x:
                print('{0} not found'.format(x))
            else:
                print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()
