"""
Problem: 10327 Flip Sort
Author : Nicolas Ibagon Rivera
"""

from sys import stdin



def merge(num, low, mid, hi):
    re = 0
    middle_1 = mid - low + 1
    middle_2 = hi- mid
    tmp = 0
    L = [0] * (middle_1)
    R = [0] * (middle_2)

    for i in range(0 , middle_1):
        L[i] = num[low + i]

    for j in range(0 , middle_2):
        R[j] = num[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i < middle_1 and j < middle_2 :
        if L[i] <= R[j]:
            num[k] = L[i]
            i += 1

        else:
            num[k] = R[j]
            j += 1
            re += middle_1-i
        k += 1


    while i < middle_1:
        num[k] = L[i]
        i += 1
        k += 1

    while j < middle_2:
        num[k] = R[j]
        j += 1
        k += 1
    return re

def mergeSort(num,low,hi):
    re = 0
    if low < hi:

        mid = int((low +(hi-1))/2)

        re = mergeSort(num, low, mid)
        re +=mergeSort(num, mid+1, hi)
        re +=merge(num, low, mid, hi)
    return re

def solve(num, low , hi ):



  re = mergeSort(num, low, hi - 1)
  return re

def main():

  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0 :
    n = int(s)
    num = [int(x) for x in inp.readline().strip().split()]

    print(lab.format(solve(num, 0, n)))

    s = inp.readline().strip()

main()
