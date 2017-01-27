# def merge_sort(input_array):
	
# 	if len(input_array) == 1:
# 		return input_array
# 	else:
# 	    mid = len(input_array) // 2
	
# 	left_half = merge_sort(input_array[:mid])
# 	right_half = merge_sort(input_array[mid:])
# 	# merge_sort_recur(left_half)
# 	# merge_sort_recur(right_half)

# 	return merge_sort(input_array)

# def merge_sort_recur(left_half,right_half):

#  i = 0
#  j = 0
#  k = 0
#  while i < len(left_half) and j < len(right_half):
#   	if left_half[i] <= right_half[j]:
#   		input_array [k] = left_half[i]
#   		i = i+1
#   	else:
#   		input_array[k] = right_half[j]
#   		j = j+1
#   	k = k+1 	
#  while i < len(left_half):
#     	input_array[k] = left_half[i]
#     	i = i+1
#     	k = k+1
#  while j < len(right_half):
#         input_array[k] = right_half[j]
#         j = j+1
#         k = k+1	
#        print merge_sort_recur(left_half,right_half)

# # def merge_sort(input_array):
	
# # 	if len(input_array) == 1:
# # 		return input_array
# # 	else:
# # 	    mid = len(input_array) // 2
	
# # 	left_half = merge_sort(input_array[:mid])
# # 	right_half = merge_sort(input_array[mid:])
# # 	# merge_sort_recur(left_half)
# # 	# merge_sort_recur(right_half)

# # 	return merge_sort(left_half,right_half)

# 	# for i in range (0,mid-1):
# 	# 	left_half[i] = input_array[i]
#  #    for i in range (mid,len(input_array)-1):
#  #    	right_half[i-mid] = input_array[i]
#  #    merge_sort_recur(left_half)
# 	# merge_sort_recur(right_half)

# input_array = map(int,raw_input('').split())
# num = merge_sort_recur(left_half,right_half)
# print num







def merge_sort(input_array,left_half,right_half):
	if len(input_array) == 1:
		return input_array
	else:
	    mid = len(input_array) // 2
	
	left_half = merge_sort(input_array[:mid])
	right_half = merge_sort(input_array[mid:])
	merge_sort(left_half)
	merge_sort(right_half)

def merge(input_array,left_half,right_half,mid):
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
       	
input_array = map(int(raw_input('').split()))
print merge_sort(input_array,left_half,right_half)
