"""
Problem: 668 - Parliament
Author : Nicolas Ibagon Rivera
"""
from sys import stdin



def solve(arr,_arr,num):

    i = 0
    cont = 0

    while num > arr[i]:
        i+=1

    cont = arr[i]

    diff = cont-num

    ans = []

    if(diff > 1):
        ans = _arr[:i+1]
        ans.remove(diff)
    elif diff == 0:
        ans = _arr[:i+1]
    else:
        ans = _arr[:i+2]
        ans.remove(2)
        ans.pop(i-1)

    return ans


def main():

    cases = stdin.readline()
    cases = int(cases)

    stdin.readline()

    _arr = [i for i in range(2,10000)]

    arr = []
    arr.append(2)
    i = 3
    while i != 10000:
        arr.append(i+arr[i-3])
        i+=1



    while cases != 0:



        num = int(stdin.readline().strip())
        stdin.readline()
        ans = solve(arr,_arr,num)

        for i in range(len(ans)):
            if(i != len(ans)-1):
                print(ans[i], end=" ")
            else:
                print(ans[i], end="")
        if(cases != 1):
            print('\n')
        cases -=1


main()
