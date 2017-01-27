# def binarySearch(input_array,val):
  
#   #while  max >= min:
#     guess_index = len(input_array) // 2 
#     sub = input_array[guess_index]
#     first_half = input_array[:guess_index]
#     second_half =input_array[guess_index:]
#     if sub==val:
#        return guess_index
#     elif sub > val:
#        return binarySearch(first_half,val)
#     elif sub < val:
#        return binarySearch(second_half,val)+len(first_half)
      

# input_array= map(int,raw_input('').split())
# val= int(raw_input(''))
# #max = len(input_array)-1
# #min = 0

# num =binarySearch(input_array,val)
# print num

    
def binarySearch(input_array,val):
  #  it will returns the index of a val (which we input) in an increasingly-sorted sequence (if exists)

  input_array = set(input_array) 
  # to avoid duplicacy because sets avoid duplicacy 

    # Converts the sequence to a list and re-sorts it. 
  sorted_input_array = sorted(input_array)

  guess_index = len(sorted_input_array) // 2
  sub = sorted_input_array[guess_index]

  first_half = sorted_input_array[:guess_index]
  second_half = sorted_input_array[guess_index:]
  if sub==val:
     return guess_index
  elif sub > val:
     return binarySearch(first_half,val)
     #it will return the index number of a val from first half of sorted_index_array.
  elif sub < val:
     return binarySearch(second_half,val)+len(first_half)


input_array= map(int,raw_input('').split())
val= int(raw_input(''))

num =binarySearch(input_array,val)
print num


 
       
