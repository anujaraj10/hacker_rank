# s=raw_input('')
# if 0<len(s)<1000:
# 	 u=s.title()
# 	 #title=it capitalize the first character of the word
# print u 

#for i in range(1,int(raw_input(''))):
 # print ([0,1,22,333,4444,55555,666666,7777777,88888888,999999999][i])
 

for i in range(1,min(int(raw_input('')),9)):
  if 1<=int(i)<=9:print int(((10**i-1)/9)*i) 


# for i in range(1,int(raw_input(''))):
#   if 1<=int(i)<=9:print sum(map(lambda x: i * 10**x, xrange(i)))


