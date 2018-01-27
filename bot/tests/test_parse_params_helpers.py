import pytest
from fixtures import params_weather_forecast
from parse_params_helpers import parse_params_weather_forecast


def test_parse_params_weather_forecast(params_weather_forecast):
    result = parse_params_weather_forecast(params_weather_forecast['param'])
    assert result == params_weather_forecast['result']
