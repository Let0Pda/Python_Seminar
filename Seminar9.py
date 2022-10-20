# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from telegram import Update


# def find_by_number(data: list, phone_number: str) -> str:
#     for el in data:
#         if el.get("Телефон") == phone_number:
#             return f'{el.get("Фамилия")}, {el.get("Имя")}'
#     return "Такой абонент отсутвует"

# ЕШЕНИЕ ДЛЯ МАК -в системном терминале вот такую команду запустили: python3 -m pip install --upgrade pip


# РЕШЕНИЕ ДЛЯ WINDOWS - В Windows при установке Python необходимо было установить галочку для установки pip, установить путь Python в папку с:\Program Files, а не в User, и обязательно поставить галочку add PATH
# pip install - r requirements.txt\
# pip install - r requirements.txt
# pip freeze
# - m venv vene

# Николай
# Групповая работа [2]

# Учимся настраивать виртуальное окружение и работать с [PIP](https://pypi.org/)

# В качестве пробы библиотек к программам предыдущего модуля подключить работу с XML \ JSON

# > Для тренировки можно создания телеграм-бота полезные ссылки:
# >
# >
# > [https://core.telegram.org/bots](https://core.telegram.org/bots)
# >
# > [https://github.com/python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
# >
# > [https://core.telegram.org/bots/api#authorizing-your-bot](https://core.telegram.org/bots/api#authorizing-your-bot)
# >
# > [https://core.telegram.org/bots/api#available-methods](https://core.telegram.org/bots/api#available-methods)
# >
# > [https://core.telegram.org/bots/api#user](https://core.telegram.org/bots/api#user)
# >
# **Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.

#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#     a) Добавьте игру против бота

#     b) Подумайте как наделить бота "интеллектом"

# Бот абв
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     msg = update.message.text
#     msg = filter(lambda x: 'ов' not in x, msg.split())
#     my = " ".join(msg)
#     await update.message.reply_text(my)

# app = ApplicationBuilder().token("Указать свой токен").build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("abc", abc))
# app.run_polling()


# def my_len(string):
#     count = 0
#     for i in string:
#         count += 1
#     return count

# def my_print(string):
#     print(string)


# name = 'Вася'

# # my_print = print(name)
# # my_len = len(name)

# # print(print(name * 2))
# # print(len(name))

# print(my_len(name))
# print(my_print(name))
# Ключевое слово await позволяет сопрограмме отдать контроль назад в главный цикл, который содержит порядок исполнения всех сопрограмм.

# async def process():
#     result = await func()
#     return result
# Если Python встречает ключевое слово await то это можно описать так: - "отложить исполнение кода сопрограммы process() до тех пор, пока я не получу результат выполнения func(). В это время я займусь чем-нибудь другим".
# pip install python-telegram-bot --pre

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# def bot_quantity():
#     global candies
#     if candies > 28:
#         candy = candies % 29
#     else:
#         candy = candies
#     # candy = random.randint(min, max)
#     # print(f"{bot}, takes {candy} candies")
#     return candy


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     global candies
#     candies = 100


# async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     global candies

#     msg = update.message.text
#     msg = msg.split()[1]
#     msg_number = int(msg)
#     candies -= msg_number
#     await update.message.reply_text(f'Осталось конфет {candies}')
#     bot_candy = bot_quantity()
#     await update.message.reply_text(f'Бот {bot_candy} конфет')
#     candies -= bot_candy
#     await update.message.reply_text(f'Осталось конфет {candies}')


# async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     msg = update.message.text
#     msg = filter(lambda x: 'ов' not in x, msg.split())
#     my = " ".join(msg)
#     await update.message.reply_text(my)

# candies = 100

# app = ApplicationBuilder().token('Ваш Токен').build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("abc", abc))
# app.add_handler(CommandHandler("new_game", new_game))
# app.add_handler(CommandHandler("game", game))
# app.run_polling()

''' 
1. Создайте программу для игры в "Крестики-нолики" при помощи виртуального окружения и PIP
2. Прикрутить бота к задачам с предыдущего семинара:
    1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
    2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
'''
