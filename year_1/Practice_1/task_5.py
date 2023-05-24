print('This is the project that reads in the radius of a circle and prints the circle’s diameter, circumference and area')
pi = 3.14159;
R = int(input('Radius = '))

L = 2 * pi * R;
d = L/pi;
S = pi * (d**2) / 4;

print('Diametr = ', d)
print('Circumference = ', L)
print('Area = ', S)

