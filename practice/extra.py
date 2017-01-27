 
#simple by applying for loop
 n=[] # take an empty list 
 for x in range(1, 100): #constraints from 1 to 100 number 
     if (x%4==0): #numbers which is divisible by 4
         n.append(x) #add numbers in to the list n 
 print (n)         


#second method
#by list comprehension method 
n=[]
int_list=([int(x) for x in range(1,100) if (x%4==0)])
n.append(x)
print int_list

