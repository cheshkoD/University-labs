import math
#Python program using loop structure to print numbers 1.2.3……9
print('#1')
for i in range(10):
    print(i)
print()

#Python program using loop structure to print numbers 9.8.7…..1
print('#2')
for i in range(10,0,-1):
    print(i)

#Python program to print on the screen odd numbers between 5..13
print('#3')
for i in range(5,13):
    if (i % 2 != 0):
        print(i)
print()

#Python program to add all the numbers entered by a user until user enters 0.
print('#4')
print("Input integers to calculate their sum. Input 0 to exit.")
a = 0
sum = 0
integer = 1
while integer != 0:
    integer = int(input(""))
    sum = sum + integer
    a += 1
if a == 0:
    print("Input some numbers")
else:
    print("The Sum of numbers are: ", sum)
print()

#Python Program to reverse a number. For example, if user enters 123 as input then 321 is printed as output.
print('#5 Python Program to reverse a number.')
b = int(input('Enter a number : '))
r = 0
while (b != 0):
    c = int(b % 10)
    r = r * 10 + c
    b = int(b / 10)
print('The reversed are:', r)
print()

#Python program to find and print factorial of a number
print('#6 Python program to find and print factorial of a number')
print('Enter the number: ')
number = int(input())
f = math.factorial(number)
print('The factorial are: ',f)
