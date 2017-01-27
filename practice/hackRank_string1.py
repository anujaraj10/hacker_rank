#swapcase
#You are given a string n.Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#constraints
#0<len(n)<=100

n=raw_input("")
if 0<len(n)<=1000:
	#length of string from 1 to 1000
	t=n.swapcase()
	#here t new variable is taken because string n is not mutable 
print t


