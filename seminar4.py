# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = 235423.2345345  # input('введите вещественное число')
# #235423.2345345.is_integer() - False
# #235423.0.is_integer() - True
# while not float(n).is_integer():
#     n *= 10
#     print(n)


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# nums = '2 54 6  7 8  89 56 5 3'
# my_list = [int(num) for num in nums.split()]
# print(min(my_list), max(my_list))


# # вариант
# i = '1 2 3 4 5 6'
# my_result = list(map(int, (i.split())))
# print(max(my_result), min(my_result))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

# a, b, с = - 2, 2, 1
# disc = b**2 - 4 * a * с  # Дискриминант
# if a == 0:
#     x = - с / b
#     print(x)
# elif disc > 0:
#     x1 = (-b - disc**0.5) / (2 * a)
#     x2 = (-b + disc**0.5) / (2 * a)
#     print(x1, x2)
# elif not disc:
#     x = -b/(2 * a)
#     print(x)
# else:
#     print("нет корней")


#     2) с помощью дополнительных библиотек Python
# Импорт библиотек
# # from sympy import *
# # from sympy.plotting import plot
# # from sympy.solvers.inequalities import solve_univariate_inequality
# init_printing(use_unicode=False, wrap_line=False, no_global=True)
# код решения, но сложно
# x = Symbol('x')
# y = Symbol('y')
# # x = -1.038
# # y = 3**0.5
# t = (2*x + 3*y)**2 - 3*x*(4/3*x+4*y)
# simplify(t)


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Чтобы получить наименьшее общее кратное в Python, мы должны применить формулу.
# НОК (a, b) = (a * b) / НОД (a, b). Здесь мы умножим a на b, а затем разделим результат
# на наибольший общий делитель (НОД) этих двух чисел.

# хорошее решение
# a, b = 1000, 1001
# nok = max(a, b)
# # while nok % a != 0 or nok % b != 0:
# while not (nok % a == 0 and nok % b == 0):
#     nok += max(a, b)
# print(nok)

# дописать
# a, b = 6, 8
# nok = a * и
# for i in range(nok, max(a, b), -1):


# измерение времени
# import time
# start_time = time.time()
# main()
# seconds = time.time() - start_time
# print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))

# ДЗ  задача 15

# k = int(input('Введите число: '))
# print(k)
# nego = [1, -1]
# fibo = [1, 1]
# for i in range(2, k):
#     lst_fibo = fibo[i-1]+fibo[i-2]
#     fibo.append(lst_fibo)
# for x, elem in enumerate(fibo, 2):
#     if x % 2 != 0:
#         lst_nego = elem * -1
#         nego.append(lst_nego)
#     else:
#         nego.append(elem)
# nego.reverse()
# nego.append(0)
# print(nego+fibo)


# def is_int(number):
#     return number.isdigit()


# def function(number):
#     if number in (1, 2):
#         return 1

#     return function(number - 1) + function(number - 2)


# number = None

# while not is_int(str(number)):
#     number = input(«Input number: »)

# number = int(number)

# result = list()
# for i in range(-number, number + 1):
#     if i != 0:
#         result.append(int(pow(i / abs(i), i + 1) * function(abs(i))))
#     else:
#         result.append(0)

# print(result)


# # задача 14 ДЗ
# n = int(input('Введите целое число: '))
# print(bin(n))
# print(f'{bin(n)[2:]}')


# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [(num % 1) for num in my_list if isinstance(num, float)] # #type(num) == float тоже самое что isinstance(num, float)]

# print(new_list)
# max_num = max(new_list)
# min_num = min(new_list)
# print(max_num - min_num)

# # 3. Задайте список из вещественных чисел.
# # Напишите программу, которая найдёт разницу между максимальным и
# # минимальным значением дробной части элементов.


# # Домашка с позицией элемента
# import random
# num = int(input('Введите число '))
# num_list = []
# for i in range(num):
#     num_list.append(random.randint(1, 10))
# print(num_list)
# print(sum(num_list[::2]))


# def get_digit(text):
#     result = text
#     if result[0] == ‘-‘:
#         result = result[1:]

#     return result.replace(‘.’, ‘’, 1)

# def is_float(number):
#     return get_digit(number).isdigit()
# Для минуса и точки

# def is_int(number):
#     return number.isdigit()

# number = None

# while not is_int(str(number)):
#     number = input(«Input number:»)
# Без try except


# https://github.com/BlackStoneShadow/Python/blob/main/Lesson3/Task4/Task4.py

# N = randint(4, 6)
# etalonlist = []
# rezlist = []
# for i in range(N):
#     etalonlist.append(randint(2, N*3))  # заполним случайными числами
# for i in range(N):
#     if (i >= N-i):
#         break
#     rezlist.append(etalonlist[i]*etalonlist[N-1-i])
# print(etalonlist, "->", rezlist)
# # так сойдет?


# def input_int(msg=""):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print("Ошибка, повторите ввод")
#         else:
#             return result


# def input_int_list():
#     count = input_int("Введите количество элементов списка: ")
#     result = []
#     for i in range(count):
#         result.append(input_int(f"Введите целое число №{i+1}: "))
#     return result

# самый простой способ Генератор списка
# lst = [randint(-10, 10) for i in range(20)]


# У меня в дз есть пример
#result = list(map(lambda i: round(i / randint(i, number), 2), range(1, number + 1)))
# Это как заполнить список
