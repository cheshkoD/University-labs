import random
# Write a function that takes two integers n and k
# and returns a number containing k of the first digits of the number n.

def get_firts_digits (n = int(input("Enter n:")), k = int(input("Enter k:"))):
    return str(n)[:k]

print(get_firts_digits())