'''Пользователь вводит месяц в виде целого числа от
1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через
list и через dict.'''

# 1 variant
month = int(input("input real number 1-12: "))
if month <= 0 or month >= 13:
    print('incorrect number')
elif month >= 3 and month <= 5:
    print('spring')
    '''здесь важно писать полное условие: "if month <= 0 or month >= 13".
    Иначе второе число питон будет считать булевым'''
elif month >= 6 and month <= 8:
    print('summer')
elif month >= 9 and month <= 11:
    print('autumn')
else:
    print('winter')

# 2 variant
from typing import Dict, Any

month = int(input("input real number 1-12: "))
if month <= 0 or month >= 13:
    print('incorrect number')

my_dict = {1: 'winter', 2: 'winter', 12: 'winter',
           3: 'spring', 4: 'spring', 5: 'spring',
           6: 'summer', 7: 'summer', 8: 'summer',
           9: 'autumn', 10: 'autumn', 11: 'autumn'}
print(my_dict.get(month))
