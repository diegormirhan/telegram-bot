from telegram.ext import Updater, CommandHandler
from config import token

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
