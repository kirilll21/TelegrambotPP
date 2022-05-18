from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from log import *


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'start {update.effective_user.first_name}')


def help_command(update: Update, context: CallbackContext):
    log(update.context)
    update.message.reply_text(f'/start\n')
