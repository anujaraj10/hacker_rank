#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014
from sys import argv
#n = raw_input('enter date format')
date = str(sys.argv[0])
month= str(sys.argv[1])
year= str(sys.argv[2])
print (date,month,year)



exam_st_date=(11,12,2016)
print ('%i / %i / %i' %exam_st_date)



