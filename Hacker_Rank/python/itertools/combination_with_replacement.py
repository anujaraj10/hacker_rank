#itertools.combinations_with_replacement
#Task
#You are given a string S. 
#Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

#Input Format
#A single line containing the string S and integer value k separated by a space.

#Output Format
#Print the combinations with their replacements of string  on separate lines.

#Sample Input
#HACK 2

from itertools import combinations_with_replacement
S,k=raw_input('').split()
k=int(k)
A=list(combinations_with_replacement(sorted(S),k))
for i in range(len(A)):
	print ("".join(A[i]))