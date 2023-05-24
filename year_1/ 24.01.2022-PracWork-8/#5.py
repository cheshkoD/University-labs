import numpy as np
# The task was:
# Create an array A [0..7] using a random number generator and display it on the screen.
# Increase all its elements in 2 times.

x = np.random.randint(0, 10, size=7)
x_2 = x * 2
print('The array is = ',x)
print('Increased elements = ',x_2)
