# - Task 5.
# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
#   Examples:
# [0, 0, 0, 1] ==> 1
# [0, 0, 1, 0] ==> 2
# [0, 1, 0, 1] ==> 5
# [1, 0, 0, 1] ==> 9
# [0, 0, 1, 0] ==> 2
# [0, 1, 1, 0] ==> 6
# [1, 1, 1, 1] ==> 15
# [1, 0, 1, 1] ==> 11

def binary_array_to_number(arr):
  return int(''.join([str(x) for x in arr]), 2)

a_binary = [0, 1, 1, 0]
a_int = binary_array_to_number(a_binary)
print('[0, 1, 1, 0] is', a_int)