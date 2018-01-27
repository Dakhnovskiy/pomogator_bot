import pytest


@pytest.fixture(
    scope='function',
    params=[
        {'param': '/погода', 'result': {'city': None, 'count_days': None}, },
        {'param': '/ПоГода', 'result': {'city': None, 'count_days': None}, },
        {'param': '/ПоГода краснодар', 'result': {'city': 'краснодар', 'count_days': None}, },
        {'param': '/погода Горячий ключ', 'result': {'city': 'Горячий ключ', 'count_days': None}, },
        {'param': '/погода Горячий ключ 10', 'result': {'city': 'Горячий ключ', 'count_days': 10}, },
        {'param': '/погода 10', 'result': {'city': None, 'count_days': 10}, },
        {'param': '/погода   10', 'result': {'city': None, 'count_days': 10}, },
        {'param': '/погода   Санкт-Петербург  10', 'result': {'city': 'Санкт-Петербург', 'count_days': 10}, },
    ],
    ids=[
        'without_param',
        'without_param_different_case',
        'city_one_word_param_different_case',
        'city_two_word_param',
        'city_two_word_and_days_param',
        'days_param',
        'days_param_with_multispace',
        'city_days_param_with_multispace',
    ]
)
def params_weather_forecast(request):
    return request.param
