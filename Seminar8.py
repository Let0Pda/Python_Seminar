# import random
# my_list = [random.randint(0,9) for x in range(random.randint(5,10))]
# odd_list = [x for n, x in enumerate(my_list) if n % 2 != 0]
# print(f'{my_list} => odd indexes has values {" и ".join(map(str, odd_list))}, sum is {sum(odd_list)}')


# collection = [2, 3, 4, 9, 1, 3]
# length = len(collection)
# print(list(map(
#     lambda i: collection[i] * collection[length - i - 1], range(length // 2 + length % 2))))


# print(*filter(lambda x: "абв" not in x, text))

# import csv
# import json
# from pathlib import Path


# def show_menu() -> int:
#     print("\n" + "=" * 20)
#     print("Выберите необходимое действие")
#     print("1. Найти сотрудника")
#     print("2. Сделать выборку сотрудников по должности")
#     print("3. Сделать выборку сотрудников по зарплате")
#     print("4. Добавить сотрудника")
#     print("5. Удалить сотрудника")
#     print("6. Обновить данные сотрудника")
#     print("7. Экспортировать данные в формате json")
#     print("8. Экспортировать данные в формате csv")
#     print("9. Закончить работу")
#     return int(input("Введите номер необходимого действия: "))

# пример json
# {"id": 1, "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432", "first_name": "\u0418\u0432\u0430\u043d \u041f\u0435\u0442\u0440\u043e\u0432\u0438\u0447",
#     "position": "\u0433\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440", "phone_number": "111", "salary": 1000.0}
# {"id": 2, "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0430", "first_name": "\u041c\u0430\u0440\u0438\u044f \u0418\u0432\u0430\u043d\u043e\u0432\u043d\u0430",
#     "position": "\u0433\u043b\u0430\u0432\u043d\u044b\u0439 \u0431\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440", "phone_number": "222", "salary": 999.99}


# пример csv
# 1	Иванов	Иван Петрович	генеральный директор	111	1000.0
# 2	Иванова	Мария Ивановна	главный бухгалтер	222	999.99

# def read_csv() -> list:
#     employee = []
#     with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
#         csv_reader = csv.reader(fin)
#         for row in csv_reader:
#             temp = {}
#             temp["id"] = int(row[0])
#             temp["last_name"] = row[1]
#             temp["first_name"] = row[2]
#             temp["position"] = row[3]
#             temp["phone_number"] = row[4]
#             temp["salary"] = float(row[5])
#             employee.append(temp)
#     return employee


# def read_json() -> list:
#     employee = []
#     with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
#         for line in fin:
#             temp = json.loads(line.strip())
#             employee.append(temp)
#     return employee


# def write_csv(employees: list):
#     with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
#         csv_writer = csv.writer(fout)
#         for employee in employees:
#             csv_writer.writerow(employee.values())


# def write_json(employees: list):
#     with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
#         for employee in employees:
#             fout.write(json.dumps(employee) + '\n')


# def read_csv(filename: str) -> list:
#     data = []
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     with open(filename, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)


# Sample Input 1:
# 2
# 1
# Sample Output 1:
# 2
# Sample Input 2:
# 5
# 2
# Sample Output 2:
# 3
# Sample Input 3:
# 7
# 5
# Sample Output 3:
# 6

# Николай
# **Задача:** Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# список и строка
# my_dict = {3: 'Иванов', 1: 'Васльев', 4: 'Петров'}


# for elem in sorted(my_dict):
#     print(elem)
#     print(elem, my_dict[elem])

# for key, value in sorted(my_dict.items()):
#     print(key, value)

# print(my_dict)
# print(sorted(my_dict))
# print(my_dict.items())
# print(type(my_dict.items()))
# print(sorted(my_dict.items()))
# print(my_dict.keys())
# print(sorted(my_dict.keys()))
# print(my_dict.values())
# print(sorted(my_dict.values()))

# my_list = [(1, 'a', True), (2, 'b', False), (3, 'x', True)]
# for first, second, third in my_list:
#     print(first)
#     print(second)
#     print(third)
#     print()
#     print('Следующй цилк')

my_dict = {'три': 'Иванов', 'один': 'Васильев',
           'четыре': 'Петров', 'шесть': 'Иванов'}
print(my_dict)

my_dict['два'] = my_dict.pop('четыре')
print(my_dict)

my_dict['три'] = my_dict['три'] + ' ' + my_dict.pop('один')
print(my_dict)

my_dict[0] = 'Привет)'
print(my_dict)

print(my_dict[1])
