
#10. Write a Python program that accept an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5 
#Expected Result : 615


n=int(5)
n1=int('%s'% n) # for a single n
n2=int('%s%s'% (n,n)) # for repeatation of nn
n3=int('%s%s%s'% (n,n,n)) # for repeatation of nnn
abc=n1+n2+n3
print (abc)


#simple implementation
n=int(raw_input(''))
n1=int(n*1)
n2=int(n**2)
n3=int(n**3)
abc=n1+n2+n3
print (abc)


#n+n^2+n^3
#n(1+n+n^2)
#n(1+n*(1+n))

#implementation using def function
import math
def abc(n):
 pqr= n*(1+n*(n+1))
 return pqr
n=int(raw_input('enter any number'))
print abc(n)
 
 
