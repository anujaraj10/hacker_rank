#mutable
#You are given an immutable string, and you want to make changes to it.

s=raw_input("")
#take a string like abrakadabra
l=list(s)
#convert the given string s into list l
a,b=(raw_input("")).split()
#take a variable a and b  with space like 5 k
a=int(a)
# variable a represent integer value lets take 5
l[a]= b 
#that means change character at position 5 with existing string of characters
s="".join(l)
#join the changed character to string s
print s