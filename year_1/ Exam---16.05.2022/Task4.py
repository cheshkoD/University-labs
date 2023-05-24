# - Task 4.
# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program
# that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

def iq_test(numbers):
    numb = [int(num)%2 for num in numbers.split(" ")]
    if numb.count(0)>1:
        return numb.index(1)+1
    else:
        return numb.index(0)+1

number_list_1 = iq_test('2 4 7 8 10')
number_list_2 = iq_test("1 2 1 1")

print(number_list_1, 'number is odd, while the rest of the numbers are even')
print(number_list_2, 'number is even, while the rest of the numbers are odd')