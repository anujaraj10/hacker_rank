#4. Write a Python program which accept the radius of a circle from the user and compute the area.


##simple implementation
pi=3.14
radius=int(raw_input("value"))
area = pi*radius** 2
print(area)




##implementation using def function
import math
def area_circle(r):
 area_of_circle= r** 2 * math.pi
 return area_of_circle

r=int(raw_input("value : "))
print(area_circle(r))

#print(area_circle(6))
