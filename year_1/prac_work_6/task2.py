# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead the empty string.

str = input("Enter a string: ")
if len(str) < 2:
      print('empty')
else:
      new_str = str[ :2 ] + str [-2: ]
print('New str is: ',new_str)
