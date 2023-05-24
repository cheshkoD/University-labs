import datetime

day, month, year = int(input('Day of Birth = ')),\
                   int(input('Month of Birth = ')),\
                   int(input('Year of Birth = '))

date_of_birth = datetime.date(year, month, day)     # 2004, 01, 01
today = datetime.date.today()                       # 2021, 11, 29
age_days = (today - date_of_birth).days             # .day -> .days
age = age_days // 365                               # здесь вместо % должно быть //
print('Your age is', age)

