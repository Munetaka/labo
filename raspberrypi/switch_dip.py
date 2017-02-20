import wiringpi as pi
import time

DIP_PIN = [14, 15, 23, 24]

STATE = ["ON", "OFF"]

dip = [0, 0, 0, 0]

pi.wiringPiSetupGpio()

for i in DIP_PIN:
    pi.pinMode(i, pi.INPUT)
    pi.pullUpDnControl(i, pi.PUD_UP)

while True:
    i = 0
    while i < len(DIP_PIN):
        dip[i] = pi.digitalRead(DIP_PIN[i])
        i = i + 1
    print("DIP1:", STATE[ dip[0] ], " DIP2:", STATE[ dip[1] ], " DIP3:", STATE[ dip[2] ], " DIP4:", STATE[ dip[3] ])
    time.sleep(1)
