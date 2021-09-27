import telegram, logging

from telegram.update import Update
from weather import cidade
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, 
    Filters,
    ConversationHandler, 
    CallbackContext
)


bot1 = telegram.Bot(token='1984131936:AAHz5tETk5Go_5wkwszNXn1WxqkpbvrztBg')


updater = Updater(token='1984131936:AAHz5tETk5Go_5wkwszNXn1WxqkpbvrztBg', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)





def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

dispatcher.add_handler(CommandHandler('start', start))


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Type /weather to set the weather!')

dispatcher.add_handler(CommandHandler('help', help))


def ask_weather(update: Update, context: CallbackContext):
    update.message.reply_text('Digite a cidade abaixo:')
    text = update.message.text

dispatcher.add_handler(CommandHandler('weather', ask_weather))


def reply_weather(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(cidade(text))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_weather))


# Mensagem caso o bot não reconheça algum comando enviado pelo usuário.
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

dispatcher.add_handler(MessageHandler(Filters.command, unknown))


print(bot1.get_me())
updater.start_polling()
updater.idle()
