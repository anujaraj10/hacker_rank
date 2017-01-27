#Find the Second Largest Number
#You are given N numbers. Store them in a list and find the second largest number.
#constraints
#2<=N<=10
#-100<=A[i]<=100


N=int(raw_input(""))
#give input N=5 
if 2<=N<=10:
	A = raw_input("") 
	#give A= 2 3 6 6 5
int_list = ([int (x) for x in A.split()])
# A[] of N integers each separated by a space.
if (-100<=i<=100 for i in int_list):
    int_list.remove (max(int_list)) 
    # remove largest number from the list
print (max(int_list))
#return largest number from the remaining list of numbers
# which is the second largest number in overall list of numbers	

