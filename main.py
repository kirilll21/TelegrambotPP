from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from commands import*
from config import TOKEN


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler())
updater.dispatcher.add_handler(CommandHandler())
updater.dispatcher.add_handler(CommandHandler())
updater.dispatcher.add_handler(CommandHandler())
updater.dispatcher.add_handler(CommandHandler())

print('бот запушен')

updater.start_polling()
updater.idle()
