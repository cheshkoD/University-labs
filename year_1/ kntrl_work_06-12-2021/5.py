# Write a program in Python that prints 10 lines with the value of Pi.
#   The first line should be 2 decimal places, the second 3 and so on.

from math import pi

for i in range(2, 12):
    line = "Pi = {:." + str(i) + "f}"

    print(line.format(pi))
