"""
Problem: 10460 - Find the Permuted String
Author : Nicolas Ibagon Rivera
"""

from sys import stdin


global factorial

factorial = [1,2,6,24,120,720,5040,40320, 362880, 3628800, 39916800,479001600, 6227020800, 87178291200,1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000,2432902008176640000, 51090942171709440000,  1124000727777607680000, 25852016738884976640000, 620448401733239439360000, 15511210043330985984000000, 403291461126605635584000000]


def permute(arr, s, N, n):

    global tmp, factorial, ans, cont, chain, flag

    if n == N:
        tmp.append(arr)
        cont += 1
        if cont == ans:
            flag = True
            chain = arr
            return
    else:
        arrN = len(arr)
        if arrN == 0:
            permute(arr+[s[0]],s,N,n+1)
        else:

            i = 0
            while i!= arrN+1 and flag != True:
                arrTmp = arr[:i] + [s[n]] + arr[i:]

                formula = (factorial[N-1]/factorial[len(arrTmp)-1]) + cont

                if formula < ans:
                    cont = formula
                else:
                    permute(arrTmp,s,N,n+1)
                i+=1
    return









def solve(s):

    global tmp, ans, cont, chain, flag

    tmp = []
    cont = 0
    chain = None
    flag = False
    permute([], s, len(s), 0)
    return chain








def main():

    global ans

    cases = int(stdin.readline())

    while cases!=0:

        s = stdin.readline().strip()
        ans = int(stdin.readline())

        answer = solve(s)



        print(''.join(answer))

        cases -=1





main()
