"""
Problem: 12785 - Emacs Plugin
Author : Nicolas Ibagon Rivera
"""


from sys import stdin


def computeFailure(p):
	m = len(p)
	j = 0
	fail = [None for _ in range(m)]
	for i in range(1,m):
		fail[i] = j
		while j > 0 and p[i] != p[j]: j = fail[j]
		j+=1
	return fail

def KMP(t,p):
	fail = computeFailure(p)
	n = len(t)
	m = len(p)
	j = 1
	i = 1
	while(i < n):
		while j > 0 and t[i] != p[j]:
			j = fail[j]
		if j ==m-1:
			return True, i
		j+=1
		i+=1
	return None, 0

def mySplit(string):
	array = []
	word = ""
	for i in range(len(string)):

		if(string[i] != "*"):
			word = word + string[i]

		if(string[i] == "*" or i == len(string)-1 ):
			if(word != ""):
				array.append(word)
				word = ""



	return array


def main():
	s = stdin.readline()
	word = stdin.readline()
	while(len(s) > 0):
		s = int(s)
		while( s > 0):
			w = mySplit(stdin.readline().strip())
			_word  = word
			if(len(w) == 0):
				print("yes")

			else:

				ans = True
				for i in range(len(w)):
						answer,position = KMP(" "+_word," "+w[i])
						ans = ans and answer
						_word = _word[position:]
				if(ans):
					print("yes")
				else:
					print("no")
			s -=1
		s = stdin.readline()
		word = stdin.readline()


main()
