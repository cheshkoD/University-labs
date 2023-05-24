# Write a function that returns the number of words in a line of text.

def count_words(str):
    total = 1
    for i in range(len(str)):
        if(str[i] == ' ' or str == '\n' or str == '\t'):
            total = total + 1
    return total

user_string = input("Enter your string: ")

res = count_words(user_string)
print("Number of words: ", res)