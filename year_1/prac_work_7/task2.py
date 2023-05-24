# Write a script that checks whether a string is a palindrome or not.
#   Returns 'True' if it is palindrome, else 'False'.
#   To check your implementation you can use strings from here
#       (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
#   The script has to ignore special characters, whitespaces and different cases

str = input('Enter the string to chek is palindrome or not: ')
str = str.casefold()
reversed_str = reversed(str)

if list(str) == list(reversed_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

