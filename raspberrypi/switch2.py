import wiringpi as pi
import time

SW_PIN = 15

pi.wiringPiSetupGpio()
pi.pinMode(SW_PIN, pi.INPUT)

pi.pullUpDnControl(SW_PIN, pi.PUD_DOWN)

while True:
    if pi.digitalRead(SW_PIN) == pi.HIGH:
        print("Switch On")
    else:
        print("Switch Off")
    time.sleep(1)
