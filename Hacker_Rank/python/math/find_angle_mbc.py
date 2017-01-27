# -- coding: cp1252
import math
degreeChar = u'\N{DEGREE SIGN}'
ab=int(raw_input(''))
if 0<ab<=100:
 bc=int(raw_input(''))
 if 0<bc<=100:
  if ab==bc:print ("45"+degreeChar)
  else:
   mc=int((math.sqrt(ab**2+bc**2))/2)
   angle=math.cos(mc/bc)
   degrees=str(int(round(math.degrees(angle))))
   print degrees+degreeChar
