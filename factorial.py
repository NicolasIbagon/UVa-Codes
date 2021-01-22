

"""
Problem: 884 - Factorial Factors
Author : Nicolas Ibagon Rivera
"""

from sys import stdin


MAX = 5001
sieve = None
prime = None
divis = None


def build_sieve_opt():
  global sieve,prime,divis
  sieve = [ True for _ in range(MAX) ] ; sieve[0] = sieve[1] = False
  divis = [ None for _ in range(MAX) ]
  prime = [ 2 ] ; divis[1] = 1 ; divis[2] = 2
  for j in range(4, MAX, 2): sieve[j],divis[j] = False,2
  for i in range(3, MAX, 2):
    if sieve[i]:
      divis[i] = i
      prime.append(i)
      for j in range(i*i, MAX, i): sieve[j],divis[j] = False,i

def factorout(n):
  global divis
  ans = dict()
  d = 0
  while n!=1:
    d,cnt = d+1,0
    while n%d==0: n,cnt = n//d,cnt+1
    ans+=cnt
  return ans




def main():

    build_sieve_opt()
    case = stdin.readline()
    caseLenght = len(case)
    ans = [0]

    for i  in range(1,MAX):

        ans.append(ans[i-1] + factorout(i))



    while caseLenght != 0:
        case = int(case)
        print(ans[case])


        case = stdin.readline()
        caseLenght = len(case)


main()
