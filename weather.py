from flask import Flask, render_template, request

import json

import urllib.request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'split'

    api_key = 'xxx'

    # source contain json data from api
    source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
        + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
