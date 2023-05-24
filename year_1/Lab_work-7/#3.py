import numpy as np
# Write a program that defines the product of two squares
# matrices 3 * 3 (dimension must be taken into account).
# Multiplication results enter the elements in the new matrix and display it on the screen.
# ------------------------------------------------------------------
array1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
array2 = np.array([[8, 9, 10], [11, 12, 13], [14, 15, 16]])
print(array1)
print('+++'*5)
print(array2)

array3 = array1 * array2
print('---'*7)
print(array3)