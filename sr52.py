import random

# 1. пользователь вводит числа до тех пор, пока не введет 0.
# После введенного 0 необходимо вывести среднее арифметическое
# всех введенных ранее чисел (не включая 0)

summa = 0
count = 0
while True:
    n = int(input())
    if n == 0:
        print(summa / count)
        break
    summa += n
    count += 1


# 2. Написать функцию, определющую минимальное значение из списка

def min_in_list(_list):
    minimum = _list[0]
    for i in _list:
        if minimum > i:
            minimum = i
    return minimum


# 3. Написать функцию, возвращающую список из 10 случайных
# значений в диапазоне от 1 до 10.

def create_list():
    return [random.randint(1, 10) for i in range(10)]


# 4. Написать функцию, принимающую в качестве аргумета два списка и
# возвращающую новый список состоящий из всех элементов этих двух списков
#
def list_append(list1, list2):
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)


# 5. Написать функцию, принимающую список и удаляющую из этого списка n-е значение

def pop_el(list1, index):
    list2 = []
    for i in range(index):
        list2.append(list1[i])
    for i in range(index + 1, len(list1)):
        list2.append((list1[i]))
    return list2


# 6. Найти индекс максимального элемента списка

def max_index(list1):
    maximum = list1[0]
    index_maximum = 0

    for i in range(len(list1)):
        if maximum < list1[i]:
            maximum = list1[i]
            index_maximum = i
    return index_maximum


# 7. Пользователь вводит сторону квадрата. Вывести треугольник вписанный в
# квадрат сл. образом:
# * * * *
# * * *
# * *
# *

side = int(input())
for i in range(side):
    for j in range(i, side):
        print("* ", end="")
    print()