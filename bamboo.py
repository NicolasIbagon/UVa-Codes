"""
Problem: 12032 The Monkey and the Oiled Bamboo
Author : Nicolas Ibagon Rivera
"""
from sys import stdin

def solve(num, n):
  temp = 0
  answer = 0

  while n > 0:
      if(len(num) == 1):
          answer = num[0]
          return answer

      else :

          temp = num[n-1] - num[n - 2]

          if(temp > answer):

              answer = temp


      n -= 1


  return answer

def main():
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    n = int(stdin.readline())
    num = [ int(x) for x in stdin.readline().split() ]
    print('Case {0}: {1}'.format(tc, solve(num, n)))

main()
