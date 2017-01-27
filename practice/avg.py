count=0
sum=0
while "true":
    inp= raw_input("enter a number")

    if inp == "done":
       break
    try:
       num= float(inp)
    except: 
       print "invalid input"
       continue
    count= count+1
    sum= sum+num
    print count,sum, num
print "average",sum/count
  

