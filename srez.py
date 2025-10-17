import random
# Контрольный срез по Python
#
#  (2б) Пользователь вводит 4 числа, найти наименьшее из них.
# a1=int(input())
# a2=int(input())
# a3=int(input())
# a4=int(input())
# minimum=a1
# if minimum>a2:
#     minimum=a2
# if minimum>a3:
#     minimum=a3
# if minimum>a4:
#     minimum=a4
# print(minimum)

# (2б) Вывести все целые числа кратные 3 в диапазоне от 0 до - 25
# (условие в цикле использовать нельзя)!

# for i in range (0, -26, -3):
#     print(i, end=" ")


# (2б) Пользователь вводит сторону квадрата. Вывести треугольник вписанный в квадрат сл. образом:
# * * * *
#   * * *
#     * *
#       *

# side = int(input())
# for i in range(side):
#     print(("  "*i)+("* "*(side-i)))

# (3б) Пользователь вводит числа до тех пор, пока не введет 0.
# Подсчитать среднее арифметическое введенных чисел.

# summa=0
# counter=0
# while True:
#     n = int(input())
#     if n==0:
#         print(summa/counter)
#         break
#     summa+=n
#     counter+=1

# (3б) Создать список из 10 элементов, заполнить его случайными
# числами в заданном пользователем диапазоне

# list1=[0,0,0,0,0,0,0,0,0,0]
# _min=int(input())
# _max=int(input())
# if _min>_max:
#     _min,_max=_max,_min
# for i in range(len(list1)):
#     list1[i]=random.randint(_min,_max)
# print(list1)
#
# list2 = [random.randint(_min,_max) for i in range (10)]
# print(list2)
# (3б) Определить индекс минимального элемента списка

# _minimum=list2[0]
# min_index=0
# for i in range (1,len(list2)):
#     if list2[i]<_minimum:
#         _minimum=list2[i]
#         min_index=i
# print(min_index)

# (3б) Напишите функцию, принимающую два одинаковых по размеру списка.
# Первый список проинициализирован, второй пустой.
# Функция должна полностью скопировать элементы первого списка во второй.

# def list_copy(list1, list2):
#     for i in range (len(list1)):
#         list2[i]=list1[i]
#
# list_copy(list1,list2)

# (4б) Напишите функцию, добавляющую элемент в i-ю позицию списка (возвращает новый список).
# def insert(list1, index, el):
#     list2=[]
#     for i in range(index):
#         list2.append(list1[i])
#     list2.append(el)
#     for i in range (index, len(list1)):
#         list2.append(list1[i])
#     return list2
#
# list4 = insert(list1, 3,234)
# print(list4)


# (6б) Используя готовые методы списков:
# Написать функцию, которая будет создавать список размером n
# и заполнять его числами в диапазоне от a до b.
# Написать функцию, принимает список и число и удаляет из списка все вхождения этого числа.

# def create_list(size, a,b):
#     return [random.randint(a, b) for i in range(size)]
#
# list5 = create_list(10,10,99)
# print(list5)
#
# list6 = [2,4,3,5,23,4,2,2,4,3]
# n=2
#
# while n in list6:
#     list6.remove(n)
# print(list6)