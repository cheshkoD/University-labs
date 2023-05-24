print('This is the Python-script that calculates the sum, difference and product of the digits of a three-digit number ')
q=int(input('Write a three digit number: '))

z = q % 10
q = q // 10
y = q % 10
x = q // 10

print('Sum of numbers = ', x+y+z)
print('Difference of numbers = ', x-y-z)
print('Product of numbers = ', x*y*z)