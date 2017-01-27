def partition(input_array,start,end):
	pivot = input_array[end];
	i = start - 1
	for j in range (start,end-1):
		if input_array[j] <= pivot:
			i = i+1
			(input_array[i],input_array[j]) = (input_array[j],input_array[i])
			(input_array[i+1],pivot) = (pivot,input_array[i+1])
			return [i+1]		
		

def quick_sort(input_array,start,end):
	if start < end:
		pivot = partition(input_array, start, end)
		quick_sort(input_array, start, pivot-1)
		quick_sort(input_array, pivot+1, end)


input_array = map(int,raw_input('').split())
start = 0
end = len(input_array)-1
quick_sort(input_array,start,end)	
print (input_array,start,end)	

