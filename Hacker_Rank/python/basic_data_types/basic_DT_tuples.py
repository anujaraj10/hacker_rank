 #tuples
 #Given an integer,n, and n space-separated integers as input, create a tuple, t, of those n integers. 
 #Then compute and print the result of hash(t).


abc=raw_input("")
#The first line contains an integer,abc, denoting the number of elements in the tuple.like abc=2 
int_list=[int(x)for x in raw_input("").split()]
# The second line contains n space-separated integers describing the elements in tuple t.like int_list= 2 3
pqr=tuple(int_list) 
 #convert list in to tuple
print hash (pqr)
 # print tuple value into hash function


# abc=raw_input("")
# for x in abc:
#  inp= x.split(abc)	
#  print inp
# pqr=tuple(inp)
# print hash (pqr) 
 


