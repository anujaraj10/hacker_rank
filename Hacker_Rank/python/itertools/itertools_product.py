#itertools.product
#Task

#You are given a two lists A and B. Your task is to compute their 
#cartesian product AXB.
#Note: A and B are sorted lists, and the cartesian product's tuples 
#should be output in sorted order.

#Input Format
#The first line contains the space separated elements of list A. 
#The second line contains the space separated elements of list B.
#Both lists have no duplicate integer elements.

#Output Format
#Output the space separated tuples of the cartesian product.

#Sample Input
#1 2
#3 4
#Sample Output
#(1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product
A=map(int,raw_input('').split())
B=map(int,raw_input('').split())
C=(list(product(A,B)))
for i in C:	
  print i,
#it will print cartesian product tuples in sorted order
# in "print i," , means output will be print as in same line  
