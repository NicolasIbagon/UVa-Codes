
"""
Problem: 914 - Jumping Champion 
Author : Nicolas Ibagon Rivera
"""


from sys import stdin





MAX = 1000010
sieve = None
prime = None
divis = None



def binary(low,hi,x):
	if hi!= 0:
		while low+1!=hi:
			mid = low + ((hi-low)>>1)
			if x < prime[mid]: hi = mid
			else: low = mid
		ans = low
	return ans


def build_sieve_opt():
  global sieve,prime,divis
  sieve = [ True for _ in range(MAX) ] ; sieve[0] = sieve[1] = False
  divis = [ None for _ in range(MAX) ]
  prime = [ 2 ] ; divis[1] = 1 ; divis[2] = 2
  for j in range(4, MAX, 2): sieve[j],divis[j] = False,2
  for i in range(3, MAX, 2):
    if sieve[i]:
      divis[i] = i
      prime.append(i)
      for j in range(i*i, MAX, i): sieve[j],divis[j] = False,i



def solve(l,u):


    repetitions = dict()



    low,hi = binary(0,len(prime),l),binary(0,len(prime),u)


    if prime[low] < l:
        low +=1

    if prime[hi] > u:
        hi-=1


    
    new_prime= prime[low:hi+1]

    for i in range(1,len(new_prime)):
        difference = new_prime[i] - new_prime[i-1]

        if difference not in repetitions:
            repetitions[difference] = 1

        else:

            repetitions[difference] += 1

    cont = 0
    maxim = -1
    ans = 0
    for i in repetitions:

        if repetitions[i] == maxim:
            cont+=1

        if repetitions[i] > maxim:
            maxim = repetitions[i]
            ans = i
            cont = 1



    if cont > 1 or ans == 0:
        print("No jumping champion")
    else:
        print("The jumping champion is {0}".format(ans))

def main():

    cases = int(stdin.readline())
    build_sieve_opt()

    while cases != 0:

        numbers = stdin.readline().strip().split()
        l,u = int(numbers[0]), int(numbers[1])

        solve(l,u)


        cases -= 1


main()
