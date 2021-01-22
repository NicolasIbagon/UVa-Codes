"""
Problem: 10701 - Pre, in and post
Author : Nicolas Ibagon Rivera
"""


from sys import stdin


def solve(preorder, inorder, n):
    root = 0
    for i in range(n):
        if preorder[0] == inorder[i]:
            root = i

    if inorder[root] != inorder[0]:
        solve(preorder[1:root+1], inorder[:root], len(preorder[1:root+1]))
    if inorder[root]!= inorder[n-1]:
        solve(preorder[root+1:], inorder[root+1:], len(preorder[root+1:]))


    print(inorder[root], end ="")
    return

def main():
    global root
    s = int(stdin.readline())
    root = 0
    while(s > 0):
        line = stdin.readline().strip().split()
        n = int(line[0])
        pre = list(line[1])
        ino = list(line[2])


        solve(pre, ino, n)
        print()
        s -= 1

main()
