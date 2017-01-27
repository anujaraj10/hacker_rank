n,m= raw_input('').split()
array=(raw_input('').split())
A=set(raw_input('').split())
B=set(raw_input('').split())
print sum([(i in A)-(i in B) for i in array])
#  For each i integer in the array, if i in A add 1. if i in set B add -1
