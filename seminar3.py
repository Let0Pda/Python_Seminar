# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# from time import time
# print(f'Случайное число от 0 до 99 = {int(time() % 1 * 100)}')

# my_time = time()
# my_time %= 1
# print(my_time)
# print(int((my_time % 1)*100))


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# my_list = ["123", "234", '12333', "567", '123']
# namber = '123'
# for i in my_list:
#     if namber in i:
#         print(i)
#         print(my_list.index(i))

# my_list = ["123","234", "12333", "567", "123"]
# number = "123"
# nul = 0
# for elem in my_list:
#     if number in elem:
#         print(elem)
#         print(my_list.index(elem, nul))
#         nul = my_list.index(elem, nul) + 1

# my_list = ["123", "234", "12333", "567", "123"]
# number = "123"
# # enumerate переберает и элементы и индексы как rage
# for i, elem in enumerate(my_list):
#     if number in elem:
#         print(elem)
#         print(i)

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# for i, elem in enumerate(my_list):
#     if number == elem and i != 0:
#         print(elem)
#         print(i)

# my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# for i in range(1, len(my_list)):
#     if number == my_list[i]:
#         print(i)

# my_list = ["123", "234", "12333", "567", "123"]
# number = my_list[0]
# print(my_list.index(number, 1))

# my_list = ["123", "234", "12333", "567", "123"]
# number = '0'
# print(my_list.index(number, 1))


###
# # 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# #     *Пример:*

# #     - 6782 -> 23
# #     - 0,56 -> 11
# # 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# #     *Пример:*

# #     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# # 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# #     *Пример:*

# #     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# # 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# # 5. Реализуйте алгоритм перемешивания списка

# from random import randint
# x = input('Введите число ')

# def summa(x):
#     if float(x) < 0:
#         x = float(x) * (-1)
#         number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number

# print(f'Сумма чисел равна {summa(x)}')

# # N = int(input('Введите число '))

# # f = 1
# # for i in range(N):
# #     i = i + 1 f = i * f

# print(f, end=" ")
# N = int(input('Введите число '))
# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
# print(f, end=" ")

# # создаём переменную N и присваем ей целочисленные значения в соответствии с вводимым через клавиатуру пользователя числом.
# N = int(input("Ввведите число: "))

# def factorial(N):  # задаём функцию факториала переменной N
#     a = 1  # создаём переменную a и присваем ей значение 1, исходя из условий задачи
#     numbers = []  # cоздаём числовую переменную, где полученные значения будут отображаться в квадратных скобках
#     for i in range(1, N+1):  # пока переменная i находится в диапозоне от 1 до N+1, то
#         a = a * i  # создаём переменную а и присваем ей произведение предыдущей переменной а * на переменную i
#     numbers.append(a)  # к числовой переменной добавляем переменную а
#     return numbers  # делаем повтор числовой переменной

# # Выводим результат решения задачи
# print(f'набор произведений чисел от 1 до N {factorial(N)}')

# # можно вообще вот так
# for i in range(2, n+1):
#     lst.append(lst[i-2] * i)

# n = int(input('Введите количество чисел в списке '))

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1}: '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна', round((numbers(n)), 2))

# def get_digit(text):
#     result = text
#     if result[0] == '-':
#         result = result[1:]

#     return result.replace('.', '', 1)

# def is_float(number):
#     return get_digit(number).isdigit()

# number = None

# while not is_float(str(number)):
#     number = input("Input number:")

# def input_int(msg):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print("Ошибка, повторите ввод: ")
#         else:
#             return result

# def generate_list(n):
#     result = []
#     for i in range(1, n+1):
#         result.append(round((1 + 1/i)**i))
#     return result

# n = input_int("Введите целое число: ")
# number_list = generate_list(n)

# print(f"Для n = {n}: {number_list} -> {sum(number_list)}")

# with open('17_Mult_task.txt', 'w') as data:
#     data.write('0\n')
#     data.write('1\n')
#     data.write('5\n')
#     data.write('8\n')
#     data.write('10\n')

# def get_numbers(n):
#     return [randint(-n/2, n) for i in range(-n, n + 1)]

# def get_data_from_file(path):
#     data = open(path, 'r')
#     dlist = [int(line.strip()) for line in data]
#     data.close()
#     return dlist

# def get_mult(numbers, datalist):
#     mult = 1
#     for i in datalist:
#         mult *= numbers[i]
#     return mult

# path = '17_Mult_task.txt'
# n = 10
# datalist = get_data_from_file(path)
# numbers = get_numbers(n)

# print(numbers)
# print(datalist)
# print(get_mult(numbers, datalist))

# N = int(input('Введите число '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
# print(numbers)

# def smes(numbers):
#     list = numbers[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(numbers))

# number = int(input('Ведите число: '))
# list = []
# for i in range(1, number+1):
#     part = [i, round((1+1/i)**i)]
#     list.append(part)
# my_dict = dict(list)
# my_sum = sum(my_dict.values())
# print(
#     f'Сумма последовательсности из {number} элементов {my_dict} равна: {my_sum}')

# def is_int(number):
#     return number.isdigit()

# number = None

# while not is_int(str(number)):
#     number = input("Input number:")

# number = int(number)

# result = dict()
# for i in range(1, number+1):
#     result[i] = round((1 + 1 / i) ** i)

# my_sum = 0
# for i in result:
#     my_sum += result[i]

# print(result, '->', my_sum)

# тemp = 0
# size = int(input("Enter a list size: "))
# numbers = list(range(size))
# print(numbers, end=" ")
# temp = 0
# for i in numbers:
#     temp = numbers[i]
#     numbers.pop(i)
#     numbers.append(temp)
# print(numbers, end=" ")

# # алгоритм перетасовки Фишера–Йейтса
# lst = [1, 2, 3, 4, 5]
# print ('Исходный список :', lst)

# for i in range(len(lst)-1, 0, -1):
#     j = random.randint(0, i + 1)   # Берем случайный индекс  от 0 до i
#     lst[i], lst[j] = lst[j], lst[i] # Меняем arr[i] с элементом случайеого индекса

# print ('перемешаный список : ', lst)

# from  random import choice
# my_list = [2,5,76,3,2,7,8,3,6,1,2,6,123]
# new_list = []
# for i in my_list:
#     new_list.append(my_list.pop(choice(my_list)))
# my_list = list(set(my_list))
