from ..config import settings
from ..db_helpers import log_request
from .parse_response_helper import parse_wiki_response
from .integration_helpers import get_parsed_response_from_sevice_or_error


def wiki_search(bot, update):
    command = 'вики'
    query = ' '.join(update.message.text.split(' ')[1:])
    params = {'search': query}
    log_request(update.message.chat_id, command, params)

    params.update({
        'action': 'opensearch',
        'format': 'xml',
        'profile': 'fuzzy',
        'limit': 1
    })

    message = get_parsed_response_from_sevice_or_error(
        settings.API_WIKI_URL,
        params,
        lambda x: parse_wiki_response(x.text)
    )

    update.message.reply_text(message)
