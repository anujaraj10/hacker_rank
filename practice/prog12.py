#12. Write a Python program to get the volume of a sphere with radius 6.

r=6
pi=3.14
volume_of_sphere= 4/3*pi*r**3
print (volume_of_sphere)


import math
math.pi
def vol(r):
 vol_of_sphere= (4/3 * pi * r** 3)
 return vol_of_sphere
r= int(raw_input('enter the value of radius'))
print vol(r)
