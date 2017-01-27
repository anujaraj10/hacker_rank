# 22. Write a Python program to count the number 4 in a given list.
count=0
abc=list()
while True:
 inp= raw_input('entr the num')
 if inp=='done':break
 value=int(inp)
 abc.append(value)#add digit in the empty list
print abc

for i in abc: #counting the no of 4 in the loop
 if (i==4):
  count=count+1
print count

