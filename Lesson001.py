# # задача 1
# a = int(input('a ='))
# b = int(input('b = '))
# if a*a == b:
#     print('Да')
# else:
#     print('нет')

# # Задача 2
# # Площадь треугольника S = 1/2 * основание * высоту

# a = int(input('a = '))
# b = int(input('b = '))
# s = 1/2 * a * b
# print(f'S = ', s)

# Задача 3
# Для подготовки к экзамену Рон каждый день учит x заклинаний, а Гермиона на y заклинаний больше.
# Сколько заклинаний они выучат вместе через n дней.
# В первой строке вводится x – количество заклинаний, которые учит Рон.
# Во второй строке y – на сколько заклинаний больше учит Гермиона.

# x = int(input('x = '))
# y = int(input('y = '))
# n = int(input('n = '))
# print(f'Sum = '(x + y) * n)

# x = int(input('Введите сколько заклинаний учит Рон: '))
# y = int(input('Введите насколько заклинаний учит Гермиона больше в день чем Рон: '))
# n = int(input('Сколько дней они учат заклинания: '))
# print(f'Рон и Гермиона за {n} дней выучат {(2*x+y)*n} заклинаний')


# задача 4
#  Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


# a1 = int(input('a1 = '))
# a2 = int(input('a2 = '))
# a3 = int(input('a3 = '))
# a4 = int(input('a4 = '))
# a5 = int(input('a5 = '))
# print(max(a1, a2, a3, a4, a5))

# list = [1, 4, 8, 7, 5]
# print(reduce(max, list))

# namber_list = list(map(int, input().split))
# print(max(namber_list))

# задача 5
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Введите число "n" '))
# for i in range(-n, n + 1):
#     print(i, end=', ') # 'end = "" ' вывод в строку


# задача 6
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
# не решил
# a = float(input('Введите число '))
# print(int(a * 10) % 10)

# Задача 7
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# a = int(input('Введите число '))
# if a % 5 == 0 and (a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print(' ДА ')
# else:
#     print(' Нет')
