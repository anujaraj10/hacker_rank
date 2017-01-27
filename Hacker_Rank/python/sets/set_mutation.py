A=raw_input('')
A=set(raw_input('').split())
N=int(raw_input(''))
N=set(raw_input('').split())
A.intersection_update(N)
print A
A.update(N)
print A
A.symmetric_difference_update(N)
print A
A.difference_update(N)
print sum(A)

