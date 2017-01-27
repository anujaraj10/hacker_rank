#abc=raw_input("enter a number")
#try:
   #xyz=int(abc)
#except:
   #xyz=1
#if xyz>0:
   #print "nice work"
#else:
   #print "not a number"


#x=0
#a=5
#b=8
#def print_add():
 #print 'a'
 #print 'b'
#print_add()
#x= a+b
#print x


#abc="   hello anuja   "
#pqr=abc.replace("anuja","raj")
#print pqr
#pqr=abc.replace('a','s')
#print pqr


####data= "mahipal anuja.raj659@gmail.com sat jan 5" 
#abc=data.find('@')
#print abc
#aab=data.find('',abc)
#print aab

name=0
abc=int(raw_input())
xyz=int(raw_input())
name=abc+xyz
print name 


total = 0
while True :
 inp = raw_input('Enter a number: ')
 if inp == 'done' : break
 value = float(inp)
 total = total + value
 add=total
print add


abc=[2,3,5,4,7,6,9,8,7,87,34,24,22]
print len(abc)
print sum(abc)
print sum(abc)/len(abc)


num=list()
while True:
 inp=raw_input("enter a number: ")
 if inp=="done":break
 value=float(inp)
 num.append(value)
add=sum(num)
print add



