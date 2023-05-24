import numpy as np
# The task was:
# Enter five integer values from the keyboard into the array.
# Print them in a single line through a comma.
# Get the arithmetic mean for the array.

x = np.array([5,10,20,30,40])
print("The mean is =",sum(x) / len(x))