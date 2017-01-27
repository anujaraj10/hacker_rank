# # # 24. Write a Python program to test whether a passed letter is a vowel or not.

# # def vowels(char): 
# #   if char == ("a"):
# #     return ("vowel")
# #   else:
# #     return ("consonant")
# #   if char == ("e"):
# #     return('vowel')
# #   else:
# #     return('consonant')
# #   if char == ("i"):
# #     return('vowel')
# #   else:
# #     return('consonant')
# #   if char == ("o"):
# #     return('vowel')
# #   else:
# #     return('consonant')
# #   if char == ("u"):
# #     return('vowel')
# #   else:
# #     return('consonant')
# # char= (raw_input('enter any alphabet'))
# # print vowels(char)

# # 24. Write a Python program to test whether a passed letter is a vowel or not.

# def vowels(char): 
#   if char == ("a"):
#     return ("vowel")
#   if char == ("e"):
#     return('vowel')
#   if char == ("i"):
#     return('vowel')
#   if char == ("o"):
#     return('vowel')
#   if char == ("u"):
#     return('vowel')
#   else:
#     return('consonant')
# char= (raw_input('enter any alphabet'))
# print vowels(char)


def vowels(char): 
  if char in ["a","e","i","o","u"]:
    print ("vowel")
  else:
    print('consonant')
char= raw_input('enter any alphabet')
print vowels(char)










