import time

import onionGpio

sleepTime = 0.5

gpio0 = onionGpio.OnionGpio(0)
gpio0.setOutputDirection(0)

ledValue = 1

while 1:
    print(ledValue)
    gpio0.setValue(ledValue)

    if ledValue == 1:
        ledValue = 0
    else:
        ledValue = 1

    time.sleep(sleepTime)
