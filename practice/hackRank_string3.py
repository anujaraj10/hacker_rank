#What's Your Name?
#You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#Hello firstname lastname! You just delved into python.
#Constraints
#The length of the first and last name ≤ 10


first_name=raw_input("")
last_name=raw_input("")
if len(first_name)<=10 and len(last_name)<=10:
  a="Hello "+ first_name +" "+ last_name +"! You just delved into python."
print a

