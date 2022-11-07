import requests
import logging
from config import TOKEN
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)

CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)
API_URL = 'https://7015.deeppavlov.ai/model'

def start():
    print('hello')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def ask_wikipedia_question(question):
    API_URL = 'https://7012.deeppavlov.ai/model'
    data = {'question_raw':  [question]}
    res = requests.post(API_URL, json=data, verify=False).json()
    return res[0][0]

async def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    # return santiment
    await Update.message.reply_text(santiment)

app = ApplicationBuilder().token(TOKEN).build()



app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("sentiment", request_sentiment))
app.run_polling()

# dispatcher = updater.dispatcher
# dispatcher.add_handler(conversation_handler)


# if __name__ == '__main__':
