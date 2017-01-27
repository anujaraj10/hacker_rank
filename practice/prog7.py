#7. Write a Python program to accept a filename from the user print the extension of that.
#Sample filename : abc.java 
#Output : java

s='abc.java'
print s[4:]



abc=raw_input('file name')
pqr=abc[4:]
print(abc)
print(pqr)


abc=raw_input('')
pqr=abc.split('.')[-1] # print only extension after "."
print(abc)
print(pqr)
