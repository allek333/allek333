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
