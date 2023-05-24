import numpy as np
# Write a program that in the matrix 4 * 4 changes all negative elements to 0
# ------------------------------------------------------------------
array = np.random.randint(-20, 20, (4, 4))
print(array)
print('--'*10)

with np.nditer(array, op_flags=['readwrite']) as elements:
    for number in elements:
        if number < 0:
            number[...] = 0
print(array)