try:
   input = raw_input("enter hours")
   hours = float(input)
   input = raw_input("enter rate")
   rate  = float(input)
except:
   print 'error enter numeric value'  



print rate,hours
if hours<=40:
   pay = rate * hours
else:   

   pay = 40+(rate*hours)
print pay          



