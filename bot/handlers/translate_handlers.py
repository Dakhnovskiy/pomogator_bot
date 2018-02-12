from ..config import settings
from ..db_helpers import log_request
from .integration_helpers import get_parsed_response_from_sevice_or_error
from .bot_states.translate_states import WAITING_INPUT

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler


def translate(bot, update):
    command = 'перевод'

    log_request(update.message.chat_id, command, {})
    languages = [
        ('Русский', 'ru'),
        ('Английский', 'en')
    ]

    keyboard = []
    for language in languages:
        keyboard.append(
            [InlineKeyboardButton(language[0], callback_data='language:%s' % language[1])]
        )

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('На какой язык будем переводить?', reply_markup=reply_markup)


def button_language(bot, update, user_data):
    query = update.callback_query
    user_data['language'] = query.data.split(':')[1]

    bot.edit_message_text(
        text='Введите текст для перевода',
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )

    return WAITING_INPUT


def translate_text(bot, update, user_data):
    yandex_link_text = 'Переведено сервисом «Яндекс.Переводчик»\nhttp://translate.yandex.ru/'
    params = {
        'key': settings.API_YANDEX_KEY,
        'lang': user_data['language'],
        'text': update.message.text,
    }

    message = get_parsed_response_from_sevice_or_error(
        url=settings.API_YANDEX_TRANSLATE_URL,
        params=params,
        parse_response_func=lambda x: '%s\n\n%s' % (''.join(x.json()['text']), yandex_link_text)
    )

    user_data.clear()

    update.message.reply_text(message)
    return ConversationHandler.END
