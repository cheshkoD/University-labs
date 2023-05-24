# Write a program in Python that determines the number of words
#   that begin and end with the same letter.

string = input("Enter a sentence: ")
words = string.split()

number = 0
for word in words:
    if (word[0].lower() == word[-1].lower()):
        number += 1
print(number)