import sys


n = float(raw_input().strip())
arr = map(int,raw_input().split(' '))
print round(len([i for i in arr if i>0])/n,3)
print round(len([i for i in arr if i<0])/n,3)
print round(len([i for i in arr if i==0])/n,3)