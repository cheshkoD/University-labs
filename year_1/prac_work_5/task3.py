# A Python program which accepts a sequence of commaseparated numbers from user and
#   generate a list and a tuple with those numbers
# Sample data : 3, 5, 7, 23
# Output:
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

numbers = input("Type numbers seperated by a comma: ")
numbers_split = numbers.split(',')
number_tuple = tuple(numbers_split)

print(number_tuple)
print(numbers_split)
