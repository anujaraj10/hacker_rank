import sys


n = int(raw_input().strip())
a = []
left_diag=sum ([a[i] [i] for i in range (n)])
right_diag=sum ([a[i] [n-1-i] for i in range (n)])
print   (abs(left_diag - right_diag))  
