import re
#Задача 3-2
#Написати програму що буде перевіряти рядок на відповідність
#дійсному числу з плаваючою комою за допомогою регулярного виразу.

regex = '[+-]?[0-9]+.[0-9]+'

def check(floatnum):
    if (re.search(regex,floatnum)):
        print('Floating point number')
    else:
        print('Not floating point number')

if __name__ == '__main__':

  floatnum ='1.20'
  check(floatnum)

  floatnum ='3'
  check(floatnum)

  floatnum ='-5.6'
  check(floatnum)
