#Python-script that detects the last 4 digits of a credit card.

print('Whrite card num:')
card_num = input()
last_digits = card_num[-4:]
print(last_digits)

#Find the sum of the digits of a three-digit number

print('White 3-digit number')
number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10
print('The sum =',a+b+c)