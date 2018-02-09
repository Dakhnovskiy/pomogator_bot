from ..db_helpers import log_request
from .notes_integration_helpers import get_notes

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def notes(bot, update):
    command = 'заметки'

    log_request(update.message.chat_id, command, {})

    keyboard = [
        [InlineKeyboardButton("Новая", callback_data='new_note')],
        [InlineKeyboardButton("Показать мои заметки", callback_data='show_notes_list')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)


def button_show_notes_list(bot, update):
    query = update.callback_query

    notes_data = get_notes(query.message.chat_id)
    keyboard = []

    for note in notes_data:
        keyboard.append([
            InlineKeyboardButton(note['title'], callback_data='show_note,%s' % note['id']),
            InlineKeyboardButton('Удалить', callback_data='delete_note,%s' % note['id'])
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup
    )


def button_new_note(bot, update):
    pass
