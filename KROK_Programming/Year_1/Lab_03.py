#
# (1)   Цілі числа:
#       Количество: 4
#       Ширина: 3
#
print('Напишите 4 целых числа: ')
integer_1=int(input())
integer_2=int(input())
integer_3=int(input())
integer_4=int(input())
print('Отформатированные значения: ')
print('Integer: ', integer_1)               #   x=
print(f'Integer: {integer_2}')              #   f'
print('Integer:{}'.format(integer_3))       #   .format
print('Integer: ', '%5.0d' % integer_4)     #   %
#
# (2)   Дійсні числа:
#       Количество: 2
#       Ширина: 8
#       Ширина поля виведення: 5
#       Кількість позицій після точки: 2
#
print('')
print('Введите 2 вещественных числа:')
real_number_1=float(input())
real_number_2=float(input())
print('Numbers with floating point: ')
print('Number: ', '{0:8}'.format(real_number_1))
print('Number: ', '{0:8}'.format(real_number_2))
print('Numbers with fixed point:')
print('Number: ', f'{real_number_1:5.2f}')
print('Number: ', f'{real_number_2:5.2f}')
#
# (3) String
#   Количество символов одной строке: 2
#
print('')
print('Введите String:')
string=input()
for i in range(0, int(len(string)/2) + 1):
    print(string[i*2:(i*2 + 2)])
#
# (4) Boolean
#
boolean = True
print('Formatted boolean: ')
print(boolean)

#
#(Переработка заданий)
#
#Методы:
#(1)
print('"x="','↓')
print('x=', integer_1,';','y=', integer_2)
print('--------------')
#(2)
print("f'",'↓')
print(f'x={integer_1}; y={integer_2}')
print('--------------')
#(3)
print("'x={}'",'↓')
print('x={}; y={}'.format(integer_1, integer_2))
print('x={1};y={0}'.format(integer_1,integer_2))
print('x={a}; y={b}'.format(a=integer_1, b=integer_2))
print('--------------')
#(4)
print("'x=%'", '↓')
print('x=\%d' % integer_1)
print('x=%d' % integer_1)
print('x=\%1.1f' % real_number_1)
print('x=%1.1f' % real_number_2)
print('--------------')
