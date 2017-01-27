#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the 
#given string. String traversal will take place from left to right, not from right to left.


S=raw_input('')
s=raw_input('')
x=0
if 1<=len(S)<=200:
	for i in range (0,len(S)):
		if S[i:].startswith(s):
			#S[i:] means omit i number uses end of string
            #startswith() checks whether string starts with str, optionally restricting the matching with the given indices start and end.
			x += 1 
			#a += b is essentially the same as a = a + b, except that:
            #+ always returns a newly allocated object, but += should (but doesn't have to) modify the object 
            #in-place if it's mutable (e.g. list or dict, but int and str are immutable).
            #In a = a + b, a is evaluated twice.
        print x			


