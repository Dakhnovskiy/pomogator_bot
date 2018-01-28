import re


def parse_params_weather_forecast(message):
    city = None
    count_days = None

    pattern = re.compile('^/\w+( +(?P<city>\D+[^ ^\d]))?( +(?P<count_days>\d+))?')
    result_search = pattern.search(message)

    if result_search:
        city = result_search.group('city')
        count_days = result_search.group('count_days')

    if count_days:
        count_days = int(count_days)

    return {'city': city, 'count_days': count_days}
