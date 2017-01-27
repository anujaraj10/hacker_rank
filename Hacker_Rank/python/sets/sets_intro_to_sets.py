
n=int(raw_input(''))
if 0<n<=100:
 height=set(map(int,raw_input().split()))
#set expected at most 1 arguments  if there are multiple arguments, map() returns a list consisting of tuples
#containing the corresponding items from all iterables (a kind of transpose operation).ex-content = map(tuple, array)
#it also happens to be one of the places where lambda routinely appears ex-list(map((lambda x: x **2), items))
#map() method is used to convert all the strings to integers.
 length=(len(height)) 
#len is a list funtion,it gives the length of a list
 average=float(sum(height))/(length)
 print average
