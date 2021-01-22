
"""
Problem: 12582 Wedding of Sultan
Author : Nicolas Ibagon Rivera
"""


from sys import stdin

def solve(array):

    pil = []
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ans = [0 for i in range(len(letters))]
    pil.append(array[0])
    for i in range(1,len(array)-1):

        if pil[-1] != array[i] and array[i] != '\n':
            ans[ord(array[i])-65] += 1
            ans[ord(pil[-1])-65] += 1
            pil.append(array[i])
        else:
            pil.pop()


    for i in range(len(ans)):
        if ans[i] != 0:
            print('{0} = {1}'.format(str(chr(i+65)),ans[i]))
    if array[0] == array[1]:
         print('{0} = {1}'.format(array[0],0))
    return




def main():

    inp = stdin
    s = int(inp.readline())
    cs= "Case {0}"
    cont =1

    while s > 0:
        array = inp.readline()
        list(array)
        print(cs.format(cont))
        solve(array)
        cont += 1
        s -= 1

main()
