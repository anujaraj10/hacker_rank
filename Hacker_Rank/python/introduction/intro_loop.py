#loop
#Read an integer N. For all non-negative integers i<N, print i^2.
#Constraints
#1<=N<=20

N=int(raw_input(""))
#enter the number 4 from user side
if 1<=N<=20:
 for i in range (0,N):
 #take a loop which traverse from 0 to N number. 
   print i**2
   #it returns square of 0,1,2,3 in vertical order.
