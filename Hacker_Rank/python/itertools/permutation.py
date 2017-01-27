#itertools.permutation
#Task
#You are given a string s. 
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

#Input Format
#A single line containing the space separated string S and the integer value k.
#Output Format
#Print the permutations of the string S on separate lines.

#Sample Input
#HACK 2

from itertools import permutations
S,k=raw_input('').split()
k=int(k)
A=list(permutations(sorted(S),k))
for i in range(len(A)):
	print ("".join(A[i]))