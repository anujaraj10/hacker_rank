n=int(raw_input(''))
if 0<=n<=1000:
 name=set()
 for i in range(n):
  name.add(raw_input())
 print len(name)