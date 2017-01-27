M=int(raw_input())
ML=set(map(int,raw_input().split()))
N=int(raw_input())
NL=set(map(int,raw_input().split()))
myset=sorted(ML.symmetric_difference(NL))
for i in (myset):print i


#The error is "invalid literal for int() with base 10:". This just means that the argument that you passed to int 
#doesn't look like a number. In other words it's either empty, or has a character in it other than a digit.