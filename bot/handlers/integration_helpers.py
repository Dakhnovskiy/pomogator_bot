import requests
from ..config import settings


def get_parsed_response_from_sevice_or_error(url, params, parse_response_func):
    response = requests.get(url, params=params)
    parsed_response = settings.ERROR_MESSAGE
    if response.status_code == 200:
        parsed_response = parse_response_func(response)

    return parsed_response
