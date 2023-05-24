# Write a program in Python that calculates the value of the function y = 4x3-2x2 + 5
#   for x values ranging from -3 to 1, in steps of 0.1.

def myrange(start, stop, step):
    while start < stop:
        yield start
        start = start + step

seq = myrange(-3, 1, 0.1)

for x in seq:
  y = 4 * x**3 - 2 * x**2 + 5
  print(y)