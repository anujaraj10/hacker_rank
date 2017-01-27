#arithmetic operators
#Read two integers from STDIN and print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
#Constraints:
#1<=a<=10^10
#1<=b<=10^10


a=int(raw_input(""))
b=int(raw_input(""))

if 1<=a<=10**10 and 1<=b<=10**10:
 print (a+b)
 print (a-b)
 print (a*b)
else:
 print ("out of order") 



