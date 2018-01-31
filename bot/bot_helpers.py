from config import settings
from telegram.ext import Updater, CommandHandler

import handlers


def get_configured_updater():
    updater = Updater(settings.BOT_TOKEN)

    updater.dispatcher.add_handler(
        CommandHandler(['погода', 'weather'], handlers.weather_forecast)
    )
    updater.dispatcher.add_handler(
        CommandHandler(['вики', 'wiki'], handlers.wiki_search)
    )
    updater.dispatcher.add_error_handler(handlers.error)
    return updater


def start_bot(updater):
    updater.start_polling()
    updater.idle()
