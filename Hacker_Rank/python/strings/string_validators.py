#You are given a string S. 
#Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters,
#digits, lowercase and uppercase characters.
#constraints
#0<len(S)<1000


S=raw_input('')
if 0<len(S)<1000:
  print any(c.isalnum() for c in S)
  #This method checks if any the characters of a string are alphanumeric (a-z, A-Z and 0-9).
  print any(c.isalpha() for c in S)
  #This method checks if any the characters of a string are alphabetical (a-z and A-Z).
  print any(c.isdigit() for c in S)
  #This method checks if any the characters of a string are digits (0-9).
  print any(c.islower() for c in S)
  #This method checks if any the characters of a string are lowercase characters (a-z).
  print any(c.isupper() for c in S)
  #This method checks if any the characters of a string are uppercase characters (A-Z).	
else: 
	print False
