
"""
Problem: 1261 - String Popping
Author : Nicolas Ibagon Rivera
"""

import sys

sys.setrecursionlimit(10000)


def solve2(s,cont, N):
    global ans


    i = 1
    while i != N and ans != True:
            if(s[i] == s[i-1]):
                cont+=1
            else:
                cont+=1
                if cont >=2:

                    newS = list(s)
                    lo = i-cont
                    hi = i
                    del newS[lo:hi]

                    cont = 0
                    if newS[0] == "c":
                        ans = True
                    else:

                        ans = ans or  solve2(newS, 0, N-(hi-lo))

                else:
                    cont = 0
            i+=1
    return ans


def main():

    cases = int(sys.stdin.readline())
    global ans
    while cases != 0:

        s = sys.stdin.readline().strip()

        s = list(s)

        s.append('c')
        ans = 0
        n = 1
        cont = 0
        N = len(s)

        if solve2(s, cont, N ):
            print(1)
        else:
            print(0)

        cases -=1



main()
