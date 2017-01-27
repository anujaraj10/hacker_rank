def linear_search(input_array,value):
	
	input_array = set(input_array)
	sort_input_array = sorted(input_array)
	for i in range (0,len(sort_input_array)):
	  if sort_input_array[i] == value:
		return i
	else:	
	    return -1

input_array = map(int,raw_input('').split())
value = int(raw_input(''))
num = linear_search(input_array,value)
print num	    	