#String Split and Join
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

n=raw_input("")
n=n.split()#Your code must be passing an empty value to split
#first line contains a string consisting of space separated words.ie my name is anuja
n="-".join(n)
#joining string n using a - hyphen.
print n
#returns output in the form of my-name-is-anuja