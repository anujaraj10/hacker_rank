#text wrap
#You are given a string S and width w. 
#Your task is to wrap the string into a paragraph of width w.


import textwrap
S=raw_input('')
w=raw_input('')
if 0<len(S)<1000 and 0<int(w)<len(S):
  print textwrap.fill(S,int(w))
  #The textwrap module provides two convenient functions: wrap() and fill().
  #The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.
   #eg abc
    #  def
    #  ghi
  #The wrap() function wraps a single paragraph in text (a string)so that every line is width characters long at most.   
    #eg ['a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 