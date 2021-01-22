
"""
Problem: 11388 - GCD LCM
Author : Nicolas Ibagon Rivera
"""

from sys import stdin




def main():



    cases = int(stdin.readline())


    while cases != 0:

        line = stdin.readline().strip().split()

        g, l = int(line[0]), int(line[1])
        if (l%g != 0):
            print("-1")
        else:
            print(g,l)
        cases -= 1







main()
