"""
Saw Yan Naung
boyermoore_SawYan.py
Lab 9

find_first - Find and return the index of the first location in the string where the pattern occurs
find_all - Find and return a list of all of the indices where the pattern occurs in the string
call_boyermoore - Call the find functions of brute force algorithm
time_boyermoore - Time the find functions of brute force algorithm

"""

import timeit

def find_first(T, P):
	"""Find and return the index of the first location in the string where the pattern occurs"""
	len_T, len_P = len(T), len(P) 
	last = {} 								# hashtable for characters in pattern
	for i in range(len_P):
		last[P[i]] = i 						# later occurrence overwrites
	count_T = count_P = len_P - 1           # index is 1 less than the actual length
	while count_T < len_T:
		if T[count_T] == P[count_P]:        # if we find a matching character
			if count_P == 0:				# if we have checked the whole pattern
				return count_T              
			else:
				count_T -= 1                # check the character before in T
				count_P -= 1                # check the character before in P
		else:
			j = last.get(T[count_T], -1)    # check the character if it is somewhere in the pattern
			count_T += len_P - min(count_P, j + 1) # case analysis for jump step
			count_P = len_P - 1             # reset so that we can check from the end of the pattern again
	raise ValueError('The pattern does not exist in the file.')

def find_all(T, P):
	"""Find and return the index of the first location in the string where the pattern occurs"""
	len_T, len_P = len(T), len(P)
	Plist = []                              # list for indexes 
	last = {} 								# hashtable for characters in pattern
	for i in range(len_P):
		last[P[i]] = i 						# later occurrence overwrites
	count_T = count_P = len_P - 1           # index is 1 less than the actual length
	while count_T < len_T:
		print(count_T)
		if T[count_T] == P[count_P]:        # if we find a matching character
			if count_P == 0:				# if we have checked the whole pattern
				Plist.append(count_T)             
			else:
				count_T -= 1                # check the character before in T
				count_P -= 1                # check the character before in P
		else:
			j = last.get(T[count_T], -1)    # check the character if it is somewhere in the pattern
			count_T += len_P - min(count_P, j + 1) # case analysis for jump step
			count_P = len_P - 1             # reset so that we can check from the end of the pattern again
			
	if len(Plist) > 0:
		return(Plist)
	else:
		raise ValueError('The pattern does not exist in the file.')		

def call_boyermoore(): 
	"""This is the function to call the find functions of brute force algorithm."""
	#X = input('Please type in the name of the file you want to use: ')
	#with open(X, 'r') as myfile:
	#with open('sequence-1.dat', 'r') as myfile:
	#	T = myfile.read().replace('\n', '')
	T = 'AACETEDEATTCATAFATTCDEG'
	P = 'ATTC'
	print('The index of the first location in T where P occurs: ', find_first(T,P))
	print('The list of indexes in T where P occurs: ',find_all(T,P))	

call_boyermoore()