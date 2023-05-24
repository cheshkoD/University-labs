import numpy as np
# The task was:
# Create an array of five last names and display them in a column,
# starting with the last.

x = np.array(['Cheshko','Bobrov','Barboskin','Shershen','Popov'])
x = x[::-1]
print('\n'.join(x))