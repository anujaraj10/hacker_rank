#  29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# color1 = ["saffron","orange","pink","blue","black","magenta"]
# color2 = ["black","blue","magenta","white","pink","orange","green"]
# common = set(color1).intersection(color2)
# print (common)


color1 = ["saffron","orange","pink","blue","black","magenta","red"]
color2 = ["black","blue","magenta","white","pink","orange","green"]
for element in color1:
 if element not in color2:
  print element
 