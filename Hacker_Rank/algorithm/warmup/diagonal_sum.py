n = int(raw_input())
dSumLeft = 0
dSumRight = 0
for i in range(n):
    matrixRow = map(int,raw_input().split(' '))
    dSumLeft = dSumLeft + matrixRow[i]
    dSumRight = dSumRight + matrixRow[n-i-1]
print abs(dSumLeft-dSumRight)
# abs function return +ve num eg abs(4-14)=10   
