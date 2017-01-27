#27. Write a Python program to concatenate all elements in a list into a string and return it.

# abc=["anuja","raj","12","mahipal","singh""08"]
# pqr="".join(abc) #concatenate string elements in a list
# print (pqr)


# abc=[1,3,4,5] # tot sum of the given elements in a list 
# pqr= sum(abc)
# result=str(pqr)
# print (result)

abc=["anuja","raj","12","mahipal","singh","08"]
pqr = ""
for x in abc:
	pqr= pqr + x
print (pqr)