# n=int(raw_input(''))
# if 1<=n<=99:
#  for i in range(1,n+1):
#    D= str(i)
#    O= oct(i)
#    H= hex(i)
#    B= bin(i)
#    print D.rjust(n)+""+O.rjust(n)+""+H.rjust(n)+""+B.rjust(n)
    


n=int(raw_input(''))
N=len(bin(n))-2
# here bin means 2 its output comes in the form of 1  1  1  1 with space between them is 2
#                                                  2  2  2  10 
if 1<=n<=99:
 for i in range(1,n+1):
 	D=str(i)
 	O=format(i,'o')
 	#convert dec into octal and remove o
 	H=format(i,'X')
 	#convert dec into hexadecimal and remove X
 	B=format(i,'b')
 	#convert dec into binary and remove b
 	print D.rjust(N),O.rjust(N),H.rjust(N),B.rjust(N)
 	#to print output in the form of right aligned i.e 1  1   1   1
 	#                                                 2  2   2  10
 	#                                                 3  3   3 011
    




# #    print (j,l)
# N = int(raw_input())
# #n = len(bin(N))-2
# for i in range(1,N+1):
#  print str(i).rjust(N) + " " + format(i,'o').rjust(N) + " " + format(i,'X').rjust(N) + " " + format(i,'b').rjust(N)
    







