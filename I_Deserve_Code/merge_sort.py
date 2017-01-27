def merge_sort(input_array):
 
 
  if len(input_array) == 1:
  	return input_array
  else:
   mid = len(input_array)// 2
   	
  left_half = input_array[:mid]
  right_half = input_array[mid:]

  merge_sort(left_half)
  merge_sort(right_half)

  i = 0
  j = 0
  k = 0
  while i < len(left_half) and j < len(right_half):
  	if left_half[i] <= right_half[j]:
  		input_array [k] = left_half[i]
  		i = i+1
  	else:
  		input_array[k] = right_half[j]
  		j = j+1
  	k = k+1 	
  while i < len(left_half):
    	input_array[k] = left_half[i]
    	i = i+1
    	k = k+1
  while j < len(right_half):
        input_array[k] = right_half[j]
        j = j+1
        k = k+1	


input_array = map(int,raw_input('').split())
merge_sort(input_array)
print (input_array)       
  	

 
  