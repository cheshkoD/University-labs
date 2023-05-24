import re
#Задача 3.1
#Написати програму, що буде перевіряти коректність номеру телефону
#за допомогою регулярного виразу.

def IsPhoneNumberValid(s):
    Pattern = re.compile("(380)?[1-9][0-9]{11}$")
    return Pattern.match(s)

#test
s = '38012345678'
if(IsPhoneNumberValid(s)):
    print('Номер дiйсний')
else:
    print('Номер не дiйсний')


