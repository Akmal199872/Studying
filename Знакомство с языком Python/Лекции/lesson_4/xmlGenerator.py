from userInterface import temperature_view
from userInterface import pressure_view
from userInterface import wind_view


def create(device = 1):
    style = 'style="font-size:22px;"'
    xml = '<xml>\n <head></head>\n <body>\n'
    xml += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    xml += '    <p {}>Wind_Speed: {} c</p>\n' \
        .format(style, wind_view(device))
    xml += '    <p {}>Pressure: {} c</p>\n' \
        .format(style, pressure_view(device))
    xml += '    </body>\n</xml>'

    with open('index.xml', 'w') as page:
        page.write(xml)

    return xml
