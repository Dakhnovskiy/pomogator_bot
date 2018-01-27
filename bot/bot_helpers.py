import os
from telegram.ext import Updater, CommandHandler

import handlers


def get_configured_updater():
    updater = Updater(os.environ.get('BOT_TOKEN'))

    updater.dispatcher.add_handler(
        CommandHandler('погода', handlers.weather_forecast)
    )
    updater.dispatcher.add_error_handler(handlers.error)
    return updater


def start_bot(updater):
    updater.start_polling()
    updater.idle()