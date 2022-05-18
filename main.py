from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from commands import *
from config import TOKEN


def check_message(update: Update, _: CallbackContext) -> None:
    text = update.message.text
    print('Пользователь написал', text)
    try:
        update.message.reply_text(weather(text))
    except Exception as e:
        print(e)
        update.message.reply_text("Я вас не понял, если вам нужна помощь введите команду /help")


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
