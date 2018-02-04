from telegram.ext import Updater, CommandHandler
from .config import settings

from .handlers import weather_forecast, wiki_search, error


def get_configured_updater():
    updater = Updater(settings.BOT_TOKEN)

    updater.dispatcher.add_handler(
        CommandHandler(['погода', 'weather'], weather_forecast)
    )
    updater.dispatcher.add_handler(
        CommandHandler(['вики', 'wiki'], wiki_search)
    )
    updater.dispatcher.add_error_handler(error)
    return updater


def start_bot(updater):
    updater.start_polling()
    updater.idle()
