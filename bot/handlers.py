import logging
import requests
import posixpath
from config import settings
from parse_params_helpers import parse_params_weather_forecast


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def weather_forecast(bot, update):
    params = parse_params_weather_forecast(update.message.text)
    weather_forecast_url = posixpath.join(
        settings.API_ENDPOINT_WEATHER_FORECAST,
        settings.API_FUNCTION_WEATHER_FORECAST
    )
    response = requests.get(weather_forecast_url, params=params)
    message = settings.ERROR_MESSAGE
    if response.status_code == 200:
        message = response.json()['description']

    update.message.reply_text(str(message).strip())

