
"""
Problem: 10344 - 23 out of 5
Author : Nicolas Ibagon Rivera
"""

from sys import stdin
from collections import deque
import itertools



def phi(pi,n,x):


    ans = False
    if(n == 1):
        ans = pi[0] == x
    else:



        value = pi.popleft()

        ans = ans or phi(pi,n-1, x-value)
        ans = ans or phi(pi,n-1, x+value)
        if(x%value == 0):  ans =  ans or phi(pi,n-1, x//value)
        pi.append(value)

    return ans





def solve(permutations,n,x):
    ans = False
    i = 0
    N = len(permutations)
    while i!= N and ans != True:

        ans = ans or phi(permutations[i],n, x )
        i+=1
    return ans


def main():

    line = stdin.readline().strip().split()
    line = list(map(int,line))
    suma = sum(line)
    while suma != 0:



        permutations = list(map(deque,itertools.permutations(line)))

        if solve(permutations,5,23):
            print("Possible")
        else:
            print("Impossible")

        line = stdin.readline().strip().split()
        line = list(map(int,line))
        suma = sum(line)





main()
