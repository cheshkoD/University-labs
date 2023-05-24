import random
# Write a function that implements a linear search for an element in a list of integers.
# If such an item is in the list, return its index, if not, return the number "-1".

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

random_arr = random.sample(range(1, 100), 20)
print(random_arr)

x = int(input("Find: "))
n = len(random_arr)

res = search(random_arr, n, x)
if (res == -1):
    print("None: ",-1)
else:
    print("Index: ", res)