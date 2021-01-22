
"""
Problem: 12485 - Perfect Choir
Author : Nicolas Ibagon Rivera
"""

from sys import stdin
import math


def solve(notes, n):
    suma =  sum(notes)
    avr =suma/n
    ans = -1

    if(suma%n == 0):
        ans = 1
        for i in range(n):
            ans += abs(avr-notes[i])
        ans = math.ceil(ans/2)


    return ans




def main():

    nNotes = stdin.readline()

    while  len(nNotes) != 0:

        nNotes = int(nNotes)

        notes = list(map(int,stdin.readline().split()))

        print(solve(notes,nNotes))
        nNotes = stdin.readline()


main()
