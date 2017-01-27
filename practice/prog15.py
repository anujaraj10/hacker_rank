# 15. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum


n1=int(raw_input('enter any number'))
n2=int(raw_input('enter any number'))
n3=int(raw_input('enter any number'))
sum= float(n1) + float(n2) + float(n3)
print (sum)



n1=2
n2=2
n3=2
sum=(n1)+(n2)+(n3)
sum1=3*sum
print (sum1)




n1=int(raw_input('enter any number'))
n2=int(raw_input('enter any number'))
n3=int(raw_input('enter any number'))
sum= (n1) + (n2) + (n3)
if n1==n2==n3:
   result= 3*(sum)
   print(result)
else:
   print(sum)   

