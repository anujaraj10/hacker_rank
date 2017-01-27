s=raw_input().upper()
vowels='AEIOU'
kevin=0
stuart=0
for i in range (len(s)):
	if 0<len(s)<=10^6:
	 if s[i] in vowels:
		kevin += len(s)-i
	 else:
	    stuart += len(s)-i
	 if kevin>stuart:
	    print "kevin",kevin
	 elif stuart>kevin:
	    print "stuart",stuart
	 else:
	    print "draw"
	                	