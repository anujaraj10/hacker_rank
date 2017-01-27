n=int(raw_input("enter the number of students"))
name=[]
grade=[]
if 2<=n<=5:
	for i in range (n):
		name.append([raw_input(""),int(raw_input(""))])
	first_lowest=[]
	second_lowest=[]
	for i in name:
		for x in first_lowest:
			del name[name.index(x)]
			del grade[grade.index(x[1])]
	for i in name:
	    if i[1]==min(grade):
	         second_lowest.append(i)
	second_lowest.sort()
for i in second_lowest:
    print i[0]



# 	A=raw_input("enter the student name")
# 	int_list=([(x) for x in A.split()])
# 	B=int(raw_input("enter the student grade"))
# 	int_list1=([int(x) for x in B.split()])
# 	print A
# 	print B
# print N
# 	


# N=int(raw_input("enter the number of students"))
# if 2<=N<=5:
# 	A=raw_input("enter the student name")
# 	for x in [A]:
# 		B=int(raw_input("enter the student grade"))
# 		for y in [B]:
#          if 2<=A<=5: 	
# 		print B
# 	print A
# print N