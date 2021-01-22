"""
Problem: 11658 - Best Coalitions
Author : Nicolas Ibagon Rivera
"""

from sys import stdin


INF = -float('Inf')
def knap(b,w,n,m,mem):
	ans = None
	
	if m in mem: ans = mem[m]
	else:
		if(n==0):
			if(m > 5000):
				ans =  (num*100)/m

			else:
				ans = 0
		else:
			ans = knap(b,w,n-1,m,mem)
			ans = max(ans, knap(b,w,n-1,m+w[n-1],mem))
		mem[m] = ans
	return ans


def main():

	line = stdin.readline().split()
	while line[0] != '0' and line[1] != '0':
		n, x = int(line[0]), int(line[1])
		numbers = []
		nu = n
		while n != 0:


			ni = float(stdin.readline().strip())
			ni = ni*100

			numbers.append(int(ni))


			n -=1
		global num
		num = numbers[x-1]

		mem = dict()
		numbers.remove(num)
		ans = round(knap(numbers, numbers, nu-1, num , mem),2)
		if ans == 100.0:
			print('100.00')
		else:
			print(ans)
		line = stdin.readline().split()



main()
