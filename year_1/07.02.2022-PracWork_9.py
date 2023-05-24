from random import random
# Fill the 10x20 matrix with random numbers from 0 to 15.
# Display the matrix itself and the line numbers in which the number 5 occurs three or more times.

N = 10
M = 20
row = []
for i in range(N):
    find_5 = 0

    for j in range(M):
        n = int(random() * 15)
        print("%3d" % n, end='')
        if n == 5:
            find_5 += 1
    print()
    if find_5 >= 3:
        row.append(i+1)

print("Строки, в которых число 5 встречаеться 3 и более раз: ",'\n',
      "(Lines in which the number 5 occurs 3 or more times:)", row)