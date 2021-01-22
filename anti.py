"""
Problem: 1235 - Anti Brute Force Lock
Author : Nicolas Ibagon Rivera
"""



from sys import stdin
from collections import deque


def vecinos(array):
    array = str(array)
    array = '0'*(4-len(array))+array
    array = list(map(int,array))
    v =[]
    for i in range(len(array)):
        if(array[i] == 9):
            n1 = 0
            n2 = array[i] - 1
        elif(array[i] == 0):
            n1 = array[i] + 1
            n2 = 9
        else:
            n1 = array[i] + 1
            n2 = array[i] - 1
        array1,array2 = array[:], array[:]
        array1[i] = n1
        array2[i] = n2
        for i in range(len(array1)):
            array1[i] = str(array1[i])
            array2[i] = str(array2[i])

        v.append(int("".join(array1)))
        v.append(int("".join(array2)))

    return v

veci = [vecinos(v) for v in range(10000)]
INF = float('inf')

def solve(n1,n2):
    global veci
    visitados = [0 for i in range(10000)]
    distancia=[INF for i in range(10000)]

    cola = deque()
    cola.append(n1)
    visitados[n1] = 1
    distancia[n1] = 0
    while len(cola):
        n = cola.popleft()
        if n == n2:
            return distancia[n2]
        for i in veci[n]:
            if visitados[i] == 0 :
                visitados[i] = 1
                cola.append(i)
            if(distancia[i] > distancia[n] + 1):
                    distancia[i] = distancia[n] + 1

    return -1


def main():
    s = int(stdin.readline())
    while( s > 0  ):
        line = stdin.readline().strip().split()
        line = list(map(int, line))
        lockers = line[0]
        line = line[1:]
        unlocked = []
        first = []
        for i in range(len(line)):
                el = map(int,str(line[i]))
                first.append(sum(el))
        key = line[first.index(min(first))]
        suma = solve(0000,key)
        unlocked.append(key)
        print(suma)

        s-=1

main()
