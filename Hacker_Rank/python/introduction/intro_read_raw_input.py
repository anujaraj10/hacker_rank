# reading raw_input
#Read a line of input from stdin and save it to a variable s, Then print the contents of s to stdout.
#Constraints
#1<=s<=500


s=raw_input("enter text")
if len(s)>=1 and len(s)<=500:
 print (s)
else:
 print ("enter number with less than 500 letters") 