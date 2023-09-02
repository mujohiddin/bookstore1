from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler
from telegram.ext.filters import Filters

from bot.handlers import start_handler, message_handler, photo_handler
def main():
    updater = Updater(token='5134440178:AAH_6rNqcXI7m4G7zFLLoX9eQfNQpUrxUH4', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(photo_handler)


    updater.start_polling()

if __name__ == '__main__':
    main()