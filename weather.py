import json
import time
import urllib3
import onionGpio

gpio0 = onionGpio.OnionGpio(0)
gpio1 = onionGpio.OnionGpio(1)

gpio0.setOutputDirection(0)
gpio1.setOutputDirection(0)


def check_weather(city='berlin'):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://forecast-weather-us.herokuapp.com/api/weather/' + city)
    json_data = json.loads(r.data)
    print json_data['temperature']
    return json_data['temperature']


temperature = check_weather()

while 1:
    current = check_weather()

    if current <= temperature:
        gpio0.setValue(1)
        gpio1.setValue(0)
        temperature = current
    else:
        gpio0.setValue(0)
        gpio1.setValue(1)
        temperature = current

    time.sleep(2)

    gpio0.setValue(0)
    gpio1.setValue(0)

    time.sleep(8)
