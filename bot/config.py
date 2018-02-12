import os


class Config(object):
    DEBUG = False
    API_ENDPOINT_WEATHER_FORECAST = 'http://127.0.0.1:5000'
    API_FUNCTION_WEATHER_FORECAST = 'v1/forecast'
    API_WIKI_URL = 'https://ru.wikipedia.org/w/api.php'
    API_NOTES_URL = 'http://127.0.0.1:8000'
    API_NOTES_HANDLER = 'api/notes'
    API_NOTES_USER = os.getenv('API_NOTES_USER')
    API_NOTES_USER_PASS = os.getenv('API_NOTES_USER_PASS')
    API_YANDEX_TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    API_YANDEX_KEY = os.getenv('API_YANDEX_KEY')

    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    ERROR_MESSAGE = 'Не удалось выполнить запрос. Попробуйте позднее'
    DATABASE = 'sqlite:///{0}'.format(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db_bot.db')
    )


class ProductionConfig(Config):
    API_ENDPOINT_WEATHER_FORECAST = 'https://weather-forecast-service.herokuapp.com'
    API_NOTES_URL = 'https://pomogator-notes-service.herokuapp.com'

    DATABASE = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True


settings_dict = {
    'DEV': DevelopmentConfig,
    'PRODUCTION': ProductionConfig
}

settings = settings_dict.get(os.environ.get('POMOGATOR_BOT_CONFIG'))
