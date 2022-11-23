from datetime import datetime

def temperature_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {}\n'
                   .format(time, data))

def pressure_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; pressure; {}\n'
                   .format(time, data))

def wind_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; wind; {}\n'
                   .format(time, data))