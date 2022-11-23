from userInterface import temperature_view
from userInterface import pressure_view
from userInterface import wind_view


def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}>Wind_Speed: {} c</p>\n' \
        .format(style, wind_view(device))
    html += '    <p {}>Pressure: {} c</p>\n' \
        .format(style, pressure_view(device))
    html += '    </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html
