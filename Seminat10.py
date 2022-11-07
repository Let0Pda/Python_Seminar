# https://demo.deeppavlov.ai/#/ru/ner
# API_URL = 'https://7015.deeppavlov.ai/model'


# обработка запроса
# def rational(update, context):
#     data = {'x': [update.message.text]}
#     res = requests.post(API_URL, json=data).json()
#     santiment = res[0][0]
#     print(res[0][0])
#     print(res)
#     update.message.reply_text(res[0][0])
#     return start(update, context)

# Обработка кнопок
# def start(update, _):
#     reply_keyboard = [['Операции с рациональными числами','Настроение', 'Операции с комплесными числами', 'Cancel']]
#     markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
#     update.message.reply_text(
#         'Добро пожаловать в калькулятор.', reply_markup=markup_key)
#     return CHOICE
# логирование
# logging.basicConfig(filename='logging.log', filemode='a',
#                         format='; '.join([
#                             f'%(asctime)s',
#                             f'%(name)s',
#                             f'%(levelname)s',
#                             f'%(message)s']),
#                         level=logging.INFO, encoding='utf-8')
# будет в файл писать логи

# доп
# logging.getLogger(__name__).info('свой текст')

# Домашка
# 1. Прикрутить бота к задачам с предыдущего семинара:
#     1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
#     2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Определяем константы этапов разговора


# CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(
#     8)


# # функция обратного вызова точки входа в разговор

# API_URL = 'https://7015.deeppavlov.ai/model'


# def ask_wikipedia_question(question):
#     API_URL = 'https://7012.deeppavlov.ai/model'
#     data = {'question_raw':  [question]}
#     res = requests.post(API_URL, json=data, verify=False).json()
#     return res[0][0]


# def request_sentiment(message):
#     data = {'x': [message]}
#     res = requests.post(API_URL, json=data).json()
#     santiment = res[0][0]
#     return santiment

# ... Николай ...
# Групповая работа [2]

# 1. Прикрутить бота к задачам с предыдущего семинара:
#     1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
#     2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
