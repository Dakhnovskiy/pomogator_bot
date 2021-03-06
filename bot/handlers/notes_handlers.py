from ..db_helpers import log_request
from .notes_integration_helpers import get_notes_by_chat_id, delete_note, get_note_text, create_note
from .bot_states.notes_states import NEW_NOTE_TEXT, NEW_NOTE_TITLE

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler


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

    notes_data = get_notes_by_chat_id(query.message.chat_id)
    if not notes_data:
        bot.edit_message_text(
            text='Заметок не найдено',
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        return

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


def button_delete_note(bot, update):
    messages = {
        True: 'Заметка удалена',
        False: 'Не удалось удалить заметку, попробуйте позднее'
    }
    query = update.callback_query

    res = delete_note(query.data.split(',')[1])

    bot.edit_message_text(
        text=messages.get(res),
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )


def button_show_note(bot, update):
    query = update.callback_query

    note_text = get_note_text(query.data.split(',')[1])

    bot.edit_message_text(
        text=note_text,
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )


def button_new_note(bot, update):
    query = update.callback_query

    bot.edit_message_text(
        text='Укажите название заметки',
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )

    return NEW_NOTE_TITLE


def new_note_title(bot, update, user_data):
    user_data['NEW_NOTE_TITLE'] = update.message.text
    update.message.reply_text('Укажите текст заметки')

    return NEW_NOTE_TEXT


def new_note_text(bot, update, user_data):
    messages = {
        True: 'Заметка создана',
        False: 'Не удалось создать заметку, попробуйте позднее'
    }

    res = create_note(
        update.message.chat_id,
        user_data['NEW_NOTE_TITLE'],
        update.message.text
    )

    update.message.reply_text(messages.get(res))
    user_data.clear()
    return ConversationHandler.END
