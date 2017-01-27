from itertools import combinations
n=[int(x) for x in raw_input().split()]
for i in n:
	if n[i]+n[i+1]==4:
 print "yes"

	# else: 
 # print "no"	
n=int(raw_input())
for i in range (1,n+1):
	#print " "*(n-i) + "#"*i
	print ('#'*i).rjust(n)