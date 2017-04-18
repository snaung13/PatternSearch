"""
Saw Yan Naung
bruteforce_SawYan.py
Lab 9

find_first - Find and return the index of the first location in the string where the pattern occurs
find_all - Find and return a list of all of the indices where the pattern occurs in the string
call_brute - Call the find functions of brute force algorithm
time_brute - Time the find functions of brute force algorithm
"""

import timeit


def find_first(T, P):
	"""Find and return the index of the first location in the string where the pattern occurs"""
	len_T, len_P = len(T), len(P)
	length = len_T - len_P + 1
	for i in range(length):
		counter = 0
		while counter < len_P and P[counter] == T[counter+i]:       # when we find a match
			counter += 1                                            # check another character in the pattern
			if counter == len_P:									# if we have checked the whole pattern
				return i
	raise ValueError('The pattern does not exist in the file.')
	
def find_all(T,P):
	"""Find and return a list of all of the indices where the pattern occurs in the string"""
	len_T, len_P = len(T), len(P)
	Plist = []
	length = len_T - len_P + 1
	for i in range(length):
		counter = 0
		while counter < len_P and P[counter] == T[counter+i]:        # when we find a match
			counter += 1                                             # check another character in the pattern
			if counter == len_P:                                     # if we have checked the whole pattern
				Plist.append(i)
	if len(Plist) > 0:
		return(Plist)
	else:
		raise ValueError('The pattern does not exist in the file.')	

def call_brute(): 
	"""This is the function to call the find functions of brute force algorithm."""
	#X = input('Please type in the name of the file you want to use: ')
	#with open(X, 'r') as myfile:
	with open('sequence-1.dat', 'r') as myfile:
		T = myfile.read().replace('\n', '')
	P = 'ATTC'
	print('The index of the first location in T where P occurs: ', find_first(T,P))
	print('The list of indexes in T where P occurs: ',find_all(T,P))

def time_brute():
	"""This is to time the find functions of brute force algorithm."""
	with open('sequence-1.dat', 'r') as myfile:
		T = myfile.read().replace('\n', '')
	shortP = 'ACG'
	longP = 'GGAGGCGGTGTTGGGACTGGAT'              # 22 characters
	shorttime, longtime = 0,0
	for i in range(0,10):						  # taking average as time taken is inconsistent
		start = timeit.default_timer()
		find_all(T,shortP)
		stop = timeit.default_timer()
		shorttime = shorttime + (stop-start)
	print("Time to find all function with a short P: " + str(shorttime/10))
	#print('The list of indexes in T where P occurs: ', find_all(T,shortP))   # Testing Purposes

	for i in range(0,10):						  # taking average as time taken is inconsistent
		start = timeit.default_timer()
		find_all(T,longP)
		stop = timeit.default_timer()
		longtime = longtime + (stop-start)
	print("Time to find all function with a long P: " + str(longtime/10))
	#print('The list of indexes in T where P occurs: ',find_all(T,longP))     # Testing Purposes


call_brute()             # Call this if you want to call the functions
time_brute()             # Call this if you want to time the functions
