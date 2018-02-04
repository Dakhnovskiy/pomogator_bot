import posixpath
from ..config import settings
from .parse_params_helpers import parse_params_weather_forecast
from ..db_helpers import get_params_from_last_request, log_request
from .integration_helpers import get_message_from_sevice_response_or_error


def weather_forecast(bot, update):
    command = 'погода'
    params = parse_params_weather_forecast(update.message.text)

    if not params['city']:
        last_params = get_params_from_last_request(update.message.chat_id, command)
        params['city'] = last_params.get('city', 'Москва')

    log_request(update.message.chat_id, command, params)

    message = get_weather_forecast(params)

    update.message.reply_text(message)


def get_weather_forecast(params):

    weather_forecast_url = posixpath.join(
        settings.API_ENDPOINT_WEATHER_FORECAST,
        settings.API_FUNCTION_WEATHER_FORECAST
    )

    return get_message_from_sevice_response_or_error(
        weather_forecast_url,
        params,
        lambda x: x.json()['description']
    )
