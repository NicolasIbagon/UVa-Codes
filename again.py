"""
Problem: 10780 - Again Prime? No Time.
Author : Nicolas Ibagon Rivera
"""


from sys import stdin




MAX = 10001
sieve = None
prime = None
divis = None
INF = float('inf')

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

def factorout(n):
  global divis, ans

  while n!=1:
    d,cnt = divis[n],0
    while n%d==0: n,cnt = n//d,cnt+1
    if d not in ans:
        ans[d] = cnt
    else:
        ans[d] += cnt
  return ans

def factorout2(n):
  global divis, ans2

  while n!=1:
    d,cnt = divis[n],0
    while n%d==0: n,cnt = n//d,cnt+1
    if d not in ans2:
        ans2[d] = cnt
    else:
        ans2[d] += cnt
  return ans2


def solve(n, m):
    global ans, ans2, ansDic

    answer = None

    if sieve[m]: answer = ansDic[n][m]
    else:
        answer = INF

        for i in ans2:
            div = ansDic[n][i]//ans2[i]
            if  div < answer:
                    answer = div




    return answer

def main():

    global ans, ans2, ansDic

    cases = int(stdin.readline())

    build_sieve_opt()
    cont = 1
    ans = dict()
    ansDic = [None]
    for i  in range(1,MAX):
        factorout(i)
        new_dic = dict(ans)
        ansDic.append(new_dic)




    while cases != 0:

        line = stdin.readline().strip().split()

        m, n = int(line[0]), int(line[1])


        ans2 = dict()


        factorout2(m)

        answer = True
        for i in ans2:
            if i not in ansDic[n]:
                answer = False

        if answer:
            print("Case {}:".format(cont))
            print(solve(n,m))
        else:
            print("Case {}:".format(cont))
            print("Impossible to divide")

        cont+=1
        cases -= 1







main()
