import math
#(1) The script that changes the values of two integer variables a and b without
#       use of additional variables.
print('Enter two numbers:')
a = int(input())
b = int(input())
a,b= b,a
print('Changed values is: ', a,",",b)

print('--------------')
#(2)  The program that calculates and displays
#       1) the arithmetic mean of two integers a and b
arifmetic_mean= (a+b)/2
print('The arifmetic meanis: ',arifmetic_mean)
#       2) geometric mean of two integers a and b
geometric_mean = math.sqrt(a*b)
print('The geometric mean is: ', geometric_mean)

print('--------------')
#(3)  The program that rearranges the digits of the three-digit number that is specified
#       user in reverse order and displays a new number on the screen.
a1 = int(input('Enter a 3-digit number: '))
r = 0
while (a1 != 0):
    c = int(a1 % 10)
    r = r * 10 + c
    a1 = int(a1 / 10)
print('The reversed number: ', r)

print('--------------')
#(4)  The program that determines the total number of hours of the day (variable hour) and
#       the total number of minutes of the day (variable minute) that have passed before the current
#           seconds of the day (variable second).
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Enter a number of seconds: "))

days = seconds // seconds_in_day
seconds = seconds - (days * seconds_in_day)
hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)
minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)
print('The currently time is:','Days:',days,',','Hours:', hours,',','Minutes:', minutes,',','Seconds:', seconds)

print('--------------')
#(5)  Write a program that determines the value of the angle in degrees between
#       clockwise at the beginning of the day and its state in hour hours, minutes
#           minutes and second seconds (0 ≤ hour ≤ 11; 0 ≤ minute; second ≤ 59).
angle = float((11 /2 * minutes - 30 * hours))
print('The angle is: ', angle)

print('--------------')
#(6)   The program that determines whether a natural number entered by the user
#       1) even
print('Enter the +number: ')
number = int(input())
if (number % 2) == 0:
   print("{0} is Even".format(number))
else:
   print("{0} is Odd".format(number))
#       2) ending in the number 5
print('The number ending on 5?')
if number % 10 == 5:
    print('True')
else:
    print('False')

print('--------------')
#   Individual task. Variant #9
#   The program, which is the lengths of the two sides of a triangle and angle (in degrees)
#       between them, finds the length of the third side and the area of it triangle.
side_c = []
print('Enter the values of sides of triangle: ')
side_a = int(input())
side_b = int(input())
print('Enter the angle between them: ')
alpha_angle = float(input())

side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(alpha_angle))     # the cosinus theorem
print('The value of third side: ',side_c)

p= (side_a + side_b + side_c)/ 2    #half-perimeter
s = math.sqrt(p*(p-side_a)*(p-side_b)*(p-side_c))
print('The value of the area of triangle: ', s)