a = list(map(int,raw_input('').split()))
a.sort()
min_sum = sum(a[0:-1])
max_sum = sum(a[1:])
print min_sum , max_sum