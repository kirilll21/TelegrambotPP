from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from log import *
from pyowm import OWM


def start(update: Update, context: CallbackContext) -> None:
    log(update, context)
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\! Если ты хочешь узнать погоду в какому нибудь городе, напиши мне название города'
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Если ты хочешь узнать погоду в своём городе напиши мне свой город!\nК примеру: Москва")


def weather(place):  # Функция с выводом погоды
    owm = OWM('18fa92788fc8f398316e9b1fc6eaeda6')  # Ваш ключ с сайта open weather map
    mgr = owm.weather_manager()  # Инициализация owm.weather_manager()
    observation = mgr.weather_at_place(place)
    # Инициализация mgr.weather_at_place() И передача в качестве параметра туда страну и город

    w = observation.weather

    status = w.detailed_status  # Узнаём статус погоды в городе и записываем в переменную status
    w.wind()  # Узнаем скорость ветра
    humidity = w.humidity  # Узнаём Влажность и записываем её в переменную humidity
    temp = w.temperature('celsius')['temp']  # Узнаём температуру в градусах по цельсию и записываем в переменную temp

    return ("В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
            "\nТемпература " + str(
                round(temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
            "\nВлажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
            "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")  # Узнаём и выводим скорость ветра
