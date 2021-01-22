"""
Problem: 10810 - Ultra-QuickSort
Author : Nicolas Ibagon Rivera
"""
from sys import stdin



def merge(array, low,mid, hi):

    re = 0
    middle_1 = mid - low + 1
    middle_2 = hi- mid
    tmp = 0
    L = [0] * (middle_1)
    R = [0] * (middle_2)

    for i in range(0 , middle_1):
        L[i] = array[low + i]

    for j in range(0 , middle_2):
        R[j] = array[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i < middle_1 and j < middle_2 :
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1

        else:
            array[k] = R[j]
            j += 1
            re += middle_1-i
        k += 1


    while i < middle_1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < middle_2:
        array[k] = R[j]
        j += 1
        k += 1
    return re


def mergeSort(array,low,hi):
    re = 0
    if low < hi:

        mid = int((low +(hi-1))/2)

        re = mergeSort(array, low, mid)
        re +=mergeSort(array, mid+1, hi)
        re +=merge(array, low, mid, hi)
    return re


def main():
  n = int(stdin.readline().strip())
  while n!=0:
    num = [ int(stdin.readline()) for _ in range(n) ]
    print(mergeSort(num,0,n-1))
    n = int(stdin.readline().strip())


main()
