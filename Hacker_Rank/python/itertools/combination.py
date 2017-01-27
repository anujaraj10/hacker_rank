#itertools.combination
#Task
#You are given a string S. 
#Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

#Input Format
#A single line containing the string S and integer value k separated by a space.
#Output Format
#Print the different combinations of string S on separate lines.

#Sample Input
#HACK 2

from itertools import combinations
S,k=raw_input('').split()
k=int(k)
for i in range(1,int(k)+1):
 A=list(combinations(sorted(S),i))
 for j in range(len(A)):
	print ("".join(A[j]))