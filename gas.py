"""
Problem: 12321 - Gas Stations
Author : Nicolas Ibagon Rivera
"""

from sys import stdin

def minIntervalos(L, G, pair):
    ans,low,n= [],0,0

    while(low < L and n != G and pair[n][0] <= low):
        best,n = n , n+1
        while(n != G and pair[n][0] <= low):
            if(pair[n][1] > pair[best][1]):
                best = n
            n += 1
        ans.append(best)
        low = pair[best][1]

    if low < L:
        ans = -1
    else:
        ans = G - len(ans)
    return ans


def main():

    line = stdin.readline().split()

    while line[0] != '0' and line[1] != '0':

        L, G = int(line[0]), int(line[1])

        g = 0
        pairs = []
        while g != G:

            gas = stdin.readline().split()

            x, r = int(gas[0]), int(gas[1])

            pairs.append((x-r,x+r))

            g+=1

        pairs.sort()
        print(minIntervalos(L, G, pairs))
        line = stdin.readline().split()



main()
