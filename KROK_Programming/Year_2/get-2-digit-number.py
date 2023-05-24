number = int(input("Введите двузначное число: "))

first_digit = number // 10
second_digit = number % 10

first_result = 2 * first_digit
second_result = 2 * second_digit

print(str(first_result) + str(second_result))