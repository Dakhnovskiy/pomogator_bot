from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from .config import settings

from .handlers import weather_forecast, wiki_search, error
from .handlers import notes, button_show_notes_list, button_new_note, button_delete_note, \
    button_show_note


def get_configured_updater():
    updater = Updater(settings.BOT_TOKEN)

    updater.dispatcher.add_handler(
        CommandHandler(['погода', 'weather'], weather_forecast)
    )
    updater.dispatcher.add_handler(
        CommandHandler(['вики', 'wiki'], wiki_search)
    )
    updater.dispatcher.add_handler(
        CommandHandler(['заметки', 'notes'], notes)
    )

    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_show_notes_list, pattern=r'^show_notes_list$')
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_new_note, pattern=r'^new_note$')
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_delete_note, pattern=r'^delete_note,\d+$')
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_show_note, pattern=r'^show_note,\d+$')
    )

    updater.dispatcher.add_error_handler(error)
    return updater


def start_bot(updater):
    updater.start_polling()
    updater.idle()
