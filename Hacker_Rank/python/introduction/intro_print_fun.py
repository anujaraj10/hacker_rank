#print function.
#Read an integer N.
#Without using any string methods, try to print the following:
#1234.........N

from __future__ import print_function
N=int(raw_input("enter the number"))
for i in range (N):
 	print (i+1,end="")
 	# end="" means result prints in the form of 123456.......N i.e in horizontal order


