
"""
Problem: 10892 - LCM Cardinality 
Author : Nicolas Ibagon Rivera
"""



from sys import stdin
from math import sqrt



def mcd(a,b):
	ans = None
	if(b == 0):
		ans = a
	else:
		ans = mcd(b,a%b)
	return ans


def mcm(a,b):


    ans = (a*b)//mcd(a,b)


    return ans






def factorout(n):

  ans = []

  for i in range(1,int(sqrt(n))+1):
      if n%i==0:
          if i not in ans:
              ans.append(i)
          if n//i not in ans:
              ans.append(n//i)
  return ans





def main():

    number = int(stdin.readline().strip())
    while number != 0:

        cont = 0
        factors = factorout(number)

        for i in range(len(factors)):
            for j in range(i,len(factors)):
                ans = mcm(factors[i],factors[j])
                if (ans == number):
                    cont+=1


        print(number, cont)
        number = int(stdin.readline().strip())









main()
