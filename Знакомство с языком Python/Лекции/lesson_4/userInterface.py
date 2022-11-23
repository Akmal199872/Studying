import dataProvider
import logger

def temperature_view(sensor):
    data = dataProvider.get_temperature(sensor)
    logger.temperature_logger(data)
    return data

def pressure_view(sensor):
    data = dataProvider.get_pressure(sensor)
    logger.pressure_logger(data)
    return data

def wind_view(sensor):
    data = dataProvider.get_wind(sensor)
    logger.wind_logger(data)
    return data
