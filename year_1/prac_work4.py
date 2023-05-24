#
# (1)   The program that reads 4 numbers
#   from the keyboard and displays the most of them on the screen.
#
print('Displays max digit of all numbers.')
a, b, c, d = (int(input('Enter digit: ')) for i in range(4))
print("Largest number is {}".format(max(a, b, c, d)))

print('------------------')
#
# (2)   Determine the number of days in a year that the user enters.
#   There are 366 days in a leap year, while there are 365 in a regular year.
#
print('The year leap or not leap.')
year = int(input('Enter the year: '))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

print('------------------')
#
# (3)   The program to indicate whether such a triangle exists or not.
#
print('Indicate whether such a triangle exists or not.')
side_a= int(input('Enter the side A: '))
side_b= int(input('Enter the side B: '))
side_c= int(input('Enter the side C: '))

if side_a + side_b > side_c and side_a + side_c > b and side_b + side_c > side_a:
    print("Treangle exist")
else:
    print("Treangle is not exist")

print('------------------')
#
# (4)   The script that print all numbers
#   in the range from 1 to 100 multiples of 7
#
print('Printing all numbers in the range from 1 to 100 multiples of 7.')
for i in range(0, 101):
    if i % 7 == 0:
        print(i)

print('------------------')
#
# (5)   Calculate the factorial of n using a loop
#
print('Calculate the factorial.')
int_f = int(input('Enter the number: '))
factorial = 1
for i in range(2, int_f+1):
    factorial = factorial * i
print('The factorial of number is: ',factorial)

print('------------------')
#
# (6)   Display the hourglass, the maximum width of which is readable from the keyboard (odd number).
#
print('Display the hourglass.')
width = int(input('Enter the width of hourglass (odd number): '))
i = 0
while i < width:
    j = 1
    while j <= width:
        if i < j <= width - i or width - i <= j <= i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j + 1
    print()
    i = i + 1

print('------------------')
#
# (7) Cycle through the display of all prime numbers from 1 to 100.
#
print('All prime numbers from 1 to 100.')
for i in range(1,101):
    for j in range(2, i):
        if i % j == 0:
          break
        else:
            print(i)
            break

print('------------------')