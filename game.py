"""
Problem: 12640 - Largest Sum Game
Author : Nicolas Ibagon Rivera
"""


from sys import stdin

def solve(num, low, hi):
  acum = 0
  ans = 0
  for i in range(hi):
      acum = acum + num[i]
      if acum < 0:
          acum = 0
      elif ans < acum:
          ans = acum
  return ans

def main():
  inp = stdin
  for line in inp.readlines():
    num = [int(x) for x in line.strip().split()]
    print(max(solve(num, 0, len(num)), 0))

main()
