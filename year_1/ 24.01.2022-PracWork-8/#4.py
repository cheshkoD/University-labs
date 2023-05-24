import numpy as np
# The task was:
# Create an array of five last names and display those
# that start with a specific letter that is entered from the keyboard.

x = np.array(['Cheshko','Bobrov','Barboskin','Shershen','Popov'])
y = input("Enter the letter: ")
for i in x:
    if y == i.lower()[0]:
        print('Surname found: ',i)
else:
    print("Surname do not found")