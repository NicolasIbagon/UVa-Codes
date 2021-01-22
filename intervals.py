"""
Problem: 12532 - Interval Product
Author : Nicolas Ibagon Rivera
"""



import sys

#Codigo tomado de 2018-2 Camilo rocha

#Clase segmentTree hecho en clase

class segmentTree:
	def __init__(self, A):
		hojas = 1
		while hojas < len(A):
			hojas*=2
		self.tree = [0 for _ in range(2*hojas)]
		self.tree[0] = 'BASURA'
		for i in range(len(A)):
			self.tree[i+hojas] = A[i]
		for i in reversed(range(1,hojas)):
			self.tree[i] = self.tree[2*i] * self.tree[2*i+1]
		self.hojas = hojas
		return
	def suma(self,lo,hi, i = 1):
		if lo==hi:
			ans = 1
		else:
			ans = self._suma(lo,hi,i=1,L=0 ,R = self.hojas)
		return ans
	def _suma(self, lo,  hi, i, L, R):
		M = (L+R)//2
		if(L == lo and R == hi):
			ans = self.tree[i]
		elif(hi<= M):
			ans = self._suma(lo,hi,2*i,L,M)
		elif(lo >= M):
			ans = self._suma(lo,hi,2*i+1,M,R)
		else:
			ans = self._suma(lo,M,2*i,L,M)
			ans *= self._suma(M,hi,2*i+1,M,R)
		return ans
	def set(self, i, val):
		i = i+self.hojas
		self.tree[i] = val
		while i!=1:
			pa = i//2
			self.tree[pa] = self.tree[2*pa] * self.tree[2*pa+1]
			i = pa
		return



def main():
    s = sys.stdin.readline().strip().split()
    s = list(map(int,s))

    while(len(s) > 0):
        numbers =  sys.stdin.readline().strip().split()
        numbers = list(map(int,numbers))
        S = segmentTree(numbers)
        k = s[1]
        while(k > 0):
            line = sys.stdin.readline().strip().split()
            line = [line[0],int(line[1]),int(line[2])]
            if(line[0] == "C"):
                S.set(line[1]-1,line[2])

            elif(line[0] == "P"):

                value = S.suma(line[1]-1,line[2])
                if(value > 0):
                    print("+",end="")
                elif(value < 0 ):
                    print("-",end="")
                else:
                    print("0",end="")
            k -=1
        print()
        s = sys.stdin.readline().strip().split()
        s = list(map(int,s))

main()
