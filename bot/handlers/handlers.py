import logging
import requests
import posixpath
from config import settings
from parse_params_helpers import parse_params_weather_forecast
from request_log_helpers import log_request
from db_query_helpers import get_params_from_last_request
from parse_response_helper import parse_wiki_response


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def weather_forecast(bot, update):
    command = 'погода'
    params = parse_params_weather_forecast(update.message.text)

    if not params['city']:
        last_params = get_params_from_last_request(update.message.chat_id, command)
        params['city'] = last_params.get('city', 'Москва')

    log_request(update.message.chat_id, command, params)

    weather_forecast_url = posixpath.join(
        settings.API_ENDPOINT_WEATHER_FORECAST,
        settings.API_FUNCTION_WEATHER_FORECAST
    )
    response = requests.get(weather_forecast_url, params=params)
    message = settings.ERROR_MESSAGE
    if response.status_code == 200:
        message = response.json()['description']

    update.message.reply_text(message)


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

    response = requests.get(settings.API_WIKI_URL, params=params)

    message = settings.ERROR_MESSAGE
    if response.status_code == 200:
        message = parse_wiki_response(response.text)

    update.message.reply_text(message)