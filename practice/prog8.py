#8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]


abc=['red','green','white','black']
print abc[0]
print abc[3]


abc=list()
while True:
 inp=raw_input('')
 if inp=='done':break
 value=str(inp)
 abc.append(value)
print (abc)
print abc[0]
print abc[-1] 
