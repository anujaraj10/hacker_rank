from time import strptime, strftime
print strftime("%H:%M:%S", strptime(raw_input(), "%I:%M:%S%p"))
#  %I=hour as a decimal number using a 12-hour clock (range 01 to 12)
#  %M=minute as a decimal number
#  %S=second as a decimal number
#  %H=hour as a decimal number using a 24-hour clock (range 00 to 23)
#  %p=either `AM' or `PM' according to the given time value, or the 
#  corresponding strings for the current locale.