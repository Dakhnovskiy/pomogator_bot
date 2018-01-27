import logging
import requests
import posixpath
import datetime


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def weather_forecast(bot, update):
    city = ' '.join(update.message.text.split(' ')[1:])
    print(update.message.text)
    message = get_weather_forecast(city)
    update.message.reply_text(str(message).strip())


def get_weather_forecast(city, count_days_for_forecast=1):
    max_count_days_for_forecast = 5
    count_days = min(max_count_days_for_forecast, count_days_for_forecast)
    max_date = datetime.datetime.today() + datetime.timedelta(days=count_days)

    api_endpoint = 'http://api.openweathermap.org'
    api_key = '24a669b0d50018deef958f24353a892c'
    api_function_current_weather = 'data/2.5/forecast'

    country = 'RU'
    city_for_find = '%s,%s' % (city, country)

    request_url = posixpath.join(api_endpoint, api_function_current_weather)
    request_params = {'q': city_for_find, 'units': 'metric', 'lang': 'ru', 'APPID': api_key}

    response = requests.get(request_url, params=request_params)
    response_json = response.json()
    weather_description_list =[]

    for row in response_json['list']:
        dt_row = datetime.datetime.fromtimestamp(row['dt'])
        if dt_row > max_date:
            continue

        dt_txt = dt_row.strftime('%d.%m.%Y %H:%M')
        temp = '{0:+3.0f}'.format(row['main']['temp'])
        weather_description = row['weather'][0]['description']
        wind_speed = row['wind']['speed']
        weather_description_list.append(
            '{date}:\nТемпература: {temp}°С\n{descr}\nCкорость ветра: {wind_speed} м/с'.format(
                date=dt_txt,
                temp=temp,
                descr=weather_description,
                wind_speed=wind_speed
            )
        )
    return '\n\n'.join(weather_description_list)
