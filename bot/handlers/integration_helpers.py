import requests
from ..config import settings


def get_message_from_sevice_response_or_error(url, params, parse_response_func):
    response = requests.get(url, params=params)
    message = settings.ERROR_MESSAGE
    if response.status_code == 200:
        message = parse_response_func(response)

    return message
