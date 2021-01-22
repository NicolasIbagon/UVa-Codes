"""
Problem: 986 - How Many?
Author : Nicolas Ibagon Rivera
"""

from sys import stdin

def phi(x,y,r,d, mem):
    key = (x,y,r,d)
    ans = 0
    if key in mem: ans = mem[key]
    else:
        if(x == 2*n):
            if(y == 0 and r == 0 and d==0):
                ans =  1

            else :
                ans =  0

        elif x != 2*n and y == 0:

            ans = phi(x+1,y+1,r, 1,mem)

        elif x != 2*n and y != 0 and (d == 0 or (d == 1 and y != k)):
            ans = phi(x+1, y+1, r, 1,mem) + phi(x+1, y-1, r, 0,mem)

        elif x != 2*n and y != 0 and d == 1 and y == k and r== 0:
            ans=phi(x+1, y+1, r, 1,mem)

        elif x!= 2*n and y != 0 and d == 1 and y == k and r != 0:
            ans = phi(x+1, y+1, r, 1,mem) + phi(x+1, y-1, r-1, 0,mem)
        mem[key] = ans
    return ans
def main():

    line =  stdin.readline().strip().split()
    
    while len(line) != 0:
        global n, r, k, key
        mem = {}
        n, r, k = int(line[0]), int(line[1]), int(line[2])




        print(phi(0,0,r,1,mem))

        line =  stdin.readline().strip().split()


main()
