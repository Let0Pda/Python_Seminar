# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#
# my_text = '1-2*3*4*2+8/4+9-3+7'
# my_list = list(my_text)
# print(my_list)

# # не рекомендуемые функции
# # my_list = eval(my_text)
# exec(f'print({my_text})')
# i = 1

# while '*' in my_list or '/' in my_list:
#     if my_list[i] == '*':
#         my_list[i - 1] = int(my_list[i - 1]) * int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     elif my_list[i] == '/':
#         my_list[i - 1] = int(my_list[i - 1]) / int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     else:
#         i += 1

# i = 1

# while '+' in my_list or '-' in my_list:
#     if my_list[i] == '+':
#         my_list[i - 1] = int(my_list[i - 1]) + int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     elif my_list[i] == '-':
#         my_list[i - 1] = int(my_list[i - 1]) - int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     else:
#         i += 1

# # for i in range(len(my_list)):
# #     if my_list[i] == '*':
# #         my_list[i - 1] = str(int(my_list[i - 1]) * int(my_list[i + 1]))
# #         my_list[i + 1] = ' '
# #         my_list[i] = ''
# #     elif my_list[i] == '/':
# #         my_list[i - 1] = str(int(my_list[i - 1]) / int(my_list[i + 1]))
# #         my_list[i + 1] = ' '
# #         my_list[i] = ''

# print(my_list)

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# #         *Пример:*
# #         1+2*3 => 7;
# #         (1+2)*3 => 9;

# Исправленный Итоговый вариант:

# def calc(my_list):
#     i = 1

#     while '*' in my_list or '/' in my_list:
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1

#     i = 1

#     while '+' in my_list or '-' in my_list:
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1
#     print('Выводим из функции результат:', my_list)
#     return my_list


# my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
# my_list_out = list(my_text)
# print(my_list_out)

# while '(' in my_list_out:
#     bracket_left = my_list_out.index('(')
#     bracket_right = my_list_out.index(')')
#     my_list_out = my_list_out[:bracket_left] + calc(
#         my_list_out[bracket_left + 1: bracket_right]) + my_list_out[bracket_right + 1:]

# print(my_text + '=>' + str(calc(my_list_out)[0]))

# ## Код Дмитрия
# my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
# my_list_out = list(my_text)
# # print(my_list_out)

# # my_list1 = eval(my_text)  # Не рекомендованная функция
# print(my_list_out)
# # exec(f'print({my_text})') # Не рекомендованная функция


# def calc(my_list):
#     i = 1

#     while '*' in my_list or '/' in my_list:
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1

#     i = 1

#     while '+' in my_list or '-' in my_list:
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1
#     return my_list


# while '(' in my_list_out:
#     bracket_left = my_list_out.index('(')
#     bracket_right = my_list_out.index(')')
#     my_list_out = my_list_out[:bracket_left] + calc(
#         my_list_out[bracket_left + 1: bracket_right]) + my_list_out[bracket_right + 1:]

# print(calc(my_list_out))
# # my_list = my_list[:до скобки] + функция(всё что в скобках) + my_list[от скобки +1:]


# альиернатива
# def split_expression(expr):
#     buffer = ""
#     result = []
#     for digit in expr:
#         if digit.isdigit():
#             buffer += digit
#         else:
#             if buffer != "":
#               result.append(int(buffer))
#             result.append(digit)
#             buffer = ""
#     result.append(int(buffer))
#     return result


# def calculate(expr_list):
#     buffer_list = expr_list.copy()
#     index = 1
#     while "*" in buffer_list or "/" in buffer_list:
#         if buffer_list[index] == "*":
#             buffer_list[index] = buffer_list[index-1]*buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "/":
#             buffer_list[index] = buffer_list[index-1]/buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     index = 1
#     while "+" in buffer_list or "-" in buffer_list:
#         if buffer_list[index] == "+":
#             buffer_list[index] = buffer_list[index-1]+buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "-":
#             buffer_list[index] = buffer_list[index-1]-buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     return buffer_list[0]


# def calculate_with_brackets(expr_list):
#     buffer_list = expr_list.copy()
#     while "(" in buffer_list:
#       start = buffer_list.index("(")
#       end = buffer_list.index(")")
#       buffer_list[start] = calculate(buffer_list[start+1:end])
#       for i in range(end, start, -1):
#         buffer_list.pop(i)
#     return calculate(buffer_list)


# expr = "1-2*3*4*2+8/4+9-3+7"
# expr_bracket = "(1-2)*3*4*2+8/(4+9-3)+7"

# print(eval(expr))
# print(calculate( split_expression(expr)))


# print(eval(expr_bracket))
# print(calculate_with_brackets(split_expression(expr_bracket)))


# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(new_list)

# # V2
# new_lst = []
# [new_lst.append(i) for i in my_list if i not in new_lst]
# print(new_list)

# V3
# enum_number = list(map(int, input("input list:").split()))
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)


# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(my_list, '=>', new_list)

# Разбор
# enum_number = [1, 2, 3, 5, 1, 5, 3, 10]
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)

# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(filter_unique)
# print(list(filter_unique))
# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(tuple(filter_unique))
# for i in filter_unique:
#     print(i)

# ### уникальные
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(range(8,-4, -1)))
# for i in range(len(my_list) - 1,-1, -1):
#     if my_list.count(my_list[i]) != 1:
#         del my_list[i]

# Домашка урок 5
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# # V1
# my_text = 'Скажика дядя ведь не даромабв Москва спалеабвнная пажаром французам отдана'
# print(my_text)

# my_list = my_text.split()
# print(my_list)

# for item in my_list:
#     if 'абв' in item:
#         my_list.remove(item)

# print(my_list)

# V2
# # 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# import random
# # generate random words from syllables
# syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
# print(random.sample(syllables, 2))
# text = list(map(lambda x: "".join(random.sample(syllables, 3)),
#             range(random.randint(12, 15))))
# print(f' TEXT : {" ".join(text)}')
# print(*text)
# # search for syllable "абв" and delete it with whole word
# parsed_text = list(x for x in text if "абв" not in x)
# print(f'PARSED: {" ".join(parsed_text)}')

# ## конфеты
# import random
# # Function checks man to take rules quantity max and min candies
# def man_quantity(min, max):
#     candy = int(input("How many candies you takes?: "))
#     while candy > max or candy < min:
#         print ("You could take more than 0 and no more than 28 candies!")
#         candy = int(input("How many candies you takes?: "))
#     return candy
# # Function bot take random candies
# def bot_quantity(min, max):
#     candy = random.randint(min, max)
#     print(f"{bot}, takes {candy} candies")
#     return candy
# # Print rules of the game
# text = "On the desk is 2021 candies.\n\
# 2 players make move one by one.\n\
# Who is first player decides the lot.\n\
# With on movie player could take no more than 28 candies\n\
# Winner is player with last move.\n\
# How many candies must take first player to win?"
# print(text)
# # Games VARS, could be changed
# candies = 221
# max = 28
# min = 1
# bot = "Bot"
# ##############################
# man = input("Enter your name: ")
# # First player random choice
# lot = random.choice([man, bot])
# if lot == bot:
#     print(f'First player is {lot}')
# else:
#     print(f"{man}, you're first player")
# # Game core
# while candies > 1:
#     if lot == bot:
#         candies -= bot_quantity(min, max)
#         if candies < 0:
#             break
#         print(f'{candies} candies left')
#         lot = man
#     else:
#         candies -= man_quantity(min, max)
#         if candies < 0:
#             break
#         print(f'{candies} candies left')
#         lot = bot

# # Who is looser :))
# print(f"{lot}, is lost, {candies} candies!")

# Крестики нолики
##
# empty_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# def print_field(field):
#     print("┌───┬───┬───┐")
#     print("│ "+" │ ".join(field[0])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[1])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[2])+" │")
#     print("└───┴───┴───┘")


# def make_move(field, move, symbol):
#     result = field.copy()
#     move = move.split()
#     [x, y] = list(map(int, move))
#     if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
#         result[y][x] = symbol
#     else:
#         new_attempt = input("Неправильный ход, повторите ввод: ")
#         result = make_move(field, new_attempt, symbol)
#     return result


# def check_win(field):
#     # проверка ряда
#     for row in field:
#         if row[0] == "X" and row[1] == "X" and row[2] == "X":
#             return "X"
#         if row[0] == "0" and row[1] == "0" and row[2] == "0":
#             return "0"
#     # проверка колонки
#     for col in range(3):
#         if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
#             return "X"
#         if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
#             return "0"
#     # проверка диагонали
#     if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
#         return "X"
#     if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
#         return "X"
#     if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     return None


# field = empty_field
# moves_count = 0
# is_X_move = True
# print("Добро пожаловать в игру X-0. В свой ход вводите координаты, разделенные пробелом.")
# while check_win(field) == None and moves_count < 9:
#     current_player = "X" if is_X_move else "0"
#     field = make_move(field, input(
#         f"Ход игрока {current_player}: "), current_player)
#     print_field(field)
#     is_X_move = not is_X_move
#     moves_count += 1
# print("Игра окончена")
# result = check_win(field)
# if result == None:
#     print("Ничья")
# else:
#     print(f"Победитель: игрок {result}")

##
# от Николая
# def field(moves):
#     y0 = f"    X1    X2   X3  "
#     y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
#     print(y0)
#     print(y1)
#     print(y1_1)
#     print(y2)
#     print(y1_1)
#     print(y3)


# def check(move, moves):
#     if len(move) == 4:
#         if move[0].lower() == 'y' and move[2].lower() == 'x':
#             if move[1] in '123' and move[-1] in '123':
#                 if moves[move[:2]][move[-2:]] == ' ':
#                     return True
#                 else:
#                     print('Данная клетка уже занята.')
#             else:
#                 print('Введены недопустимые значения координат.')
#         else:
#             print('Вы ввели не допустимые оси координат')
#     else:
#         print('Введено недопустимое количество символов.')
#     print('Попробуйте ещё раз!')
#     return False


# def wins(moves):
#     if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
#             or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
#             or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
#             and moves['y1']['x1'] != ' '):
#         return moves['y1']['x1']
#     elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
#            or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
#            or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
#           and moves['y2']['x2'] != ' '):
#         return moves['y2']['x2']
#     elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
#            or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
#           and moves['y3']['x3'] != ' '):
#         return moves['y3']['x3']
#     return False


# def move(symbol, moves, player):
#     print('Текущий ход y{}x{}'.format(player[1], player[-1]))
#     if player[1] == '1':
#         if player[-1] == '1':
#             moves['y1']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y1']['x2'] = symbol
#         else:
#             moves['y1']['x3'] = symbol
#     elif player[1] == '2':
#         if player[-1] == '1':
#             moves['y2']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y2']['x2'] = symbol
#         else:
#             moves['y2']['x3'] = symbol
#     else:
#         if player[-1] == '1':
#             moves['y3']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y3']['x2'] = symbol
#         else:
#             moves['y3']['x3'] = symbol
#     return moves


# moves_out = {
#     'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
# }

# field(moves_out)

# number_players = int(input('Введите количество игроков (1/2): '))
# count_move = 0

# if number_players == 2:
#     win = False
#     while not win and count_move < 9:
#         count_move += 1
#         player_out = input('Введите координаты хода(пример - y2x3): ')
#         while not check(player_out, moves_out):
#             player_out = input('Введите координаты хода(пример - y2x3): ')
#         if count_move % 2:
#             symbol_out = 'X'
#         else:
#             symbol_out = 'O'
#         moves_out = move(symbol_out, moves_out, player_out)

#         field(moves_out)
#         win = wins(moves_out)
#     if count_move == 9:
#         print('Ничья!')
#     else:
#         print(f'На {count_move} ходу победили "{win}"')


# def encoding(text):
#     code_text = ""
#     count = 0
#     repetitions = 1
#     while count < len(text):
#         try:
#             if text[count] == text[count+1]:
#                 repetitions += 1
#             elif repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#                 repetitions = 1
#         except IndexError:
#             if repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#         count += 1
#     return code_text
# # Function to decode given cipher


# def decoding(cipher):
#     decoded_text = ""
#     count = 0
#     repetitions = 0
#     while count < len(cipher):
#         if str(cipher[count]).isdigit():
#             repetitions = int(cipher[count])
#         elif repetitions > 0:
#             for x in range(repetitions):
#                 decoded_text += cipher[count]
#                 repetitions = 0
#         elif repetitions == 0:
#             decoded_text += cipher[count]
#         count += 1
#     return decoded_text


# # Text input
# text = input("Enter a text: ")
# # Decides encode or decode
# numbers_in_text = 0
# for num in text:
#     if num.isdigit():
#         numbers_in_text += 1
# # If any digits exists it mean coded text, decoding
# if numbers_in_text > 0:
#     print(f"Decoding: {decoding(text)}")
# # If no digits exists it mean pure text, encoding
# else:
#     print(f"Encoding: {encoding(text)}")
from math import ceil

x = int(2021 % 29)
y = 745 % 29
k = 1*29 - 28
print(x)
print(y)
print(k)
