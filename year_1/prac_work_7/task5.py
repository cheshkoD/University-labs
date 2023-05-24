# For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.
#   Example:
#       n = 1234 result = 4
#       n = 246 result = 0

n = int(input('Enter the integer: '))
s = 0
while n > 0:
    r = n % 10
    if r % 2 != 0:
        s = s + r
    n = int(n / 10)

print("Sum of odd digits:", s)
