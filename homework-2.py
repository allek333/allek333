# TASK 1
'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
 а указать явно, в программе.'''
my_list = ['list', 32, 3.3, True]
for i in my_list:
    print(type(i))

# TASK 2
'''2)Для списка реализовать обмен значений соседних
элементов, т.е. Значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для
заполнения списка элементов необходимо использовать
функцию input().'''

list = [i for i in input('input list of data: ').split()]
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i-1]
print(list)
# print(type(i))
''' ".split"  разделяет по пробелу, т.е. он возвращает список из слов в строке. '''

# TASK 3
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
print (my_dict.get(month))

# TASK 4
'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

# variant 1
my_list = input('input text: ')
words = my_list.split()
print(words)
n = 1
for i in words:
    print(n, i[:10])
    n += 1

'''n=0
while n < len(words):
    print(n+1, words[:10])
    break
    Неправильный вариант. Цикл не работает'''

variant 2
my_list = input('enter: ')
words = my_list.split()
print(words)
for i, words in enumerate(words, start = 1):
    print(i, words[:10])
    '''Здесь важно указать в цикле "i" и "words". Это для функции enumerate,
    чтобы она не только разделила, но и пронумеровала каждое значение.
    Здесь i будет обращение к общему выводу цикла, это будет главным
    аргументом для цикла. Words будет
    аргументом, по которому работает цикл и записывает в i'''

# TASK 5
'''5)	Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют
элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
my_number = input('num ')
for i, number in enumerate(my_list):
    if int(my_number) < int(number):
        continue
    my_list.insert(i, my_number)
    break
    print(my_list)
else:
    my_list.append(my_number)
print(my_list)


