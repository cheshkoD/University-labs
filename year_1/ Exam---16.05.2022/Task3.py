# - Task 3.
# Write a function using recursion to check if a number n is prime
# (you have to check whether n is divisible by any number below n).

def chek_a_number(numb, i=2):
    if (numb <= 2):
        return True if (n == 2) else False
    if (numb % i == 0):
        return False
    if (i * i > numb):
        return True
    return chek_a_number(numb, i + 1)

numb = int(input('Enter the number : '))
if (chek_a_number(numb)):
    print(numb ,'- is prime number')
else:
    print(numb ,'- is non prime number')