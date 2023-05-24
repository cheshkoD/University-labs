# Implement a script which returns the longest word in the given string.
#   The word can contain any symbols except whitespaces (`,\n,\tand so on).
#   If there are multiple longest words in the string with a same length return the word that occurs first.

str = input("Enter sentence: ")
longest = max(str.split(), key=len)
print("Longest word is: ", longest)
