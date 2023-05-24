
x, y, z = 10, 5, -4

#(1)Assume that we define x, y, and z to refer to int values. Write an expression that computes whether...
   #(1.1)...x is odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   #(1.2)...x is a multiple of 20
numb = int(input("Enter a number: "))
if (numb % 20) ==0:
   print("{0} Multiple of 20".format(numb))
else:
   print("{0} NonMultiple of 20".format(numb))
print('--------------------')

#(2)Assume that zero is a positive number. Write an expression that computes whether...
   #(2.1)...x and y are both positiv
print(f' X ({x}) and Y ({y}) both positive?: { x >= 0 and y >= 0 }')
   #(2.2)...x and y have the same sign
print(f' X ({x}) and Y ({y}) have the same sign?: { (x >= 0 and y >= 0) or (x <= 0 and y <= 0) }')
   #(2.3)...x and y have different signs
print(f' X ({x}) and Y ({y}) have different signs?: { (x >= 0 >= y) or (x <= 0 <= y) }')
print('--------------------')

#(3)Write an expression that computes whether...
   #(3.1)...all three names (x, y, and z) are bound to equal values
print(f'All three variables (x, y and z) are bound to equal values?: { x is y is z }')
   #(3.2)...all three names (x, y, and z) are bound to different values (none the same)
print(f'All three variables (x, y and z) are bound to different values?: { x is not y is not z }')
   #(3.3)...


