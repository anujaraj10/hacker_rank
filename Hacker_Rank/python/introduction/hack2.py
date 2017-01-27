# n= int(raw_input('enter any number'))
# if 1<=n<=100:
#  	print n
# else: 
#      print ("out of range")	
# if n%2==0 and 2<=n<=5:
#     print ("not weird")
# else: 
#     n%2!=0 and n<=19
#     print ("weird")
# if  n%2==0 and 6<=n<=20:
#     print ("weird")
# else:
#      n%2==0 and n>20
#      print ("not weird")    




n= int(raw_input('enter any number'))
if 1<=n<=100:
  	print n
else: 
    print ("out of range")	
 if (n%2!=0) or (n%2==0 and n in range (6,20)):
    print ("weird")
 else: 
   (n%2==0) and (2<=n<=5) or (n>20)
   print ("not weird")



n= int(raw_input(''))
if 1<=n<=100:
 if (n%2!=0) or (n%2==0 and n in range (6,20)):
    print ("weird")
 else: 
    (n%2==0 and ((n in range (2,5)) or n>20))
    print ("not weird")
              
              
