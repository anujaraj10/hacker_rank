#list comprehension
#You are given three integers x,y and z representing the dimensions of a cuboid. You have to print a list of all possible coordinates 
#on a 3D grid where the sum of xi+yi+zi is not equal to n. If x=2, the possible values of xi can be 0,1 and 2. The same applies to y and z.

x,y,z,n= int(raw_input("")),int(raw_input("")),int(raw_input("")),int(raw_input(""))
#sample input= 1 1 1 2 i.e for x y z=1 and for n= 2
int_list = ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)  if a +b+c!=n])
#(0,x+1),(0,y+1) and (0,z+1) means list in lexicographic increasing order.
print (int_list)
# print output in the form of [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

