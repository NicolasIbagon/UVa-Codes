"""
Problem: 112 - Tree Summing
Author : Nicolas Ibagon Rivera
"""



import sys
from collections import deque

sys.setrecursionlimit(10000)

def solve(tree, acum, num):
    global bool
    if(len(tree) > 0):
            sum = acum + tree[0]
            if(sum != num):
                acum += tree[0]
                solve(tree[1], acum, num)
                solve(tree[2],acum, num)
            elif(sum == num and (len(tree[1]) == 0 and len(tree[2]) == 0)):
                bool = True
            elif(sum == num and (len(tree[1]) > 0 or len(tree[2]) > 0)):
                solve(tree[1],sum,num)
                solve(tree[2],sum,num)
    return



def parse():
    global dq
    c = dq.popleft()
    if  c == "(":
        T = []
        if(dq[0].isdigit() or dq[0] == '-'):
            T.append(int(readInt()))
        while dq[0]!= ')':
            x = parse()
            T.append(x)
        dq.popleft()
    return T

def readInt():
    global s, dq
    if(len(dq) > 0):
        c = dq.popleft()
        if(c.isdigit() or c == '-'):
            s = "" + c
            n = dq[0]
            if(n.isdigit()):
                s += readInt()
    else:

        s=""
    return s


def main():
    global bool, dq
    s = sys.stdin.read().replace("\n","").replace(" ","")

    dq = deque(s)
    while (len(dq) > 0):
            num = int(readInt())

            tree = parse()
            bool = False
            solve(tree,0,num)
            if(bool):
                print("yes")
            else:
                print("no")

main()
