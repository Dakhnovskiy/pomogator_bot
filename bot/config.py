import os


class Config(object):
    DEBUG = False
    API_ENDPOINT_WEATHER_FORECAST = 'http://127.0.0.1:5000'
    API_FUNCTION_WEATHER_FORECAST = 'v1/forecast'
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    ERROR_MESSAGE = 'Не удалось выполнить запрос. Попробуйте позднее'
    DATABASE = 'sqlite:///{0}'.format(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db_bot.db')
    )


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


settings_dict = {
    'DEV': DevelopmentConfig,
    'PRODUCTION': ProductionConfig
}

settings = settings_dict.get(os.environ.get('POMOGATOR_BOT_CONFIG'))
