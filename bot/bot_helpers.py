from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, \
    MessageHandler, Filters
from .config import settings

from .handlers import weather_forecast, wiki_search, error
from .handlers import notes, button_show_notes_list, button_new_note, button_delete_note, \
    button_show_note, new_note_title, new_note_text

from .handlers.bot_states.notes_states import NEW_NOTE_TITLE, NEW_NOTE_TEXT

from .handlers import translate, translate_text, button_language
from .handlers.bot_states.translate_states import WAITING_INPUT


def add_wiki_handlers(updater):
    updater.dispatcher.add_handler(
        CommandHandler(['погода', 'weather'], weather_forecast)
    )


def add_weather_handlers(updater):
    updater.dispatcher.add_handler(
        CommandHandler(['вики', 'wiki'], wiki_search)
    )


def add_notes_handlers(updater):
    updater.dispatcher.add_handler(
        CommandHandler(['заметки', 'notes'], notes)
    )

    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_show_notes_list, pattern=r'^show_notes_list$')
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_show_note, pattern=r'^show_note,\d+$')
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(button_delete_note, pattern=r'^delete_note,\d+$')
    )

    updater.dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CallbackQueryHandler(button_new_note, pattern=r'^new_note$')],

            states={
                NEW_NOTE_TITLE: [MessageHandler(Filters.text, new_note_title, pass_user_data=True)],
                NEW_NOTE_TEXT: [MessageHandler(Filters.text, new_note_text, pass_user_data=True)],
            },

            fallbacks=[]
        )
    )


def add_translate_handlers(updater):
    updater.dispatcher.add_handler(
        CommandHandler(['перевод', 'translate'], translate)
    )

    updater.dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CallbackQueryHandler(button_language, pattern=r'^language:.+$', pass_user_data=True)],

            states={
                WAITING_INPUT: [MessageHandler(Filters.text, translate_text, pass_user_data=True)],
            },

            fallbacks=[]
        )
    )


def get_configured_updater():
    updater = Updater(settings.BOT_TOKEN)

    add_wiki_handlers(updater)
    add_weather_handlers(updater)
    add_notes_handlers(updater)
    add_translate_handlers(updater)

    updater.dispatcher.add_error_handler(error)
    return updater


def start_bot(updater):
    updater.start_polling()
    updater.idle()
