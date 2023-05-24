# Write a program that displays the elements of a linear
# array (array elements are user-defined) in reverse order.
# ------------------------------------------------------------------
list = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    elem = int(input())
    list.append(elem)  # adding the element
print('list: ',list)

list.reverse()
print('reversed list: ', list)