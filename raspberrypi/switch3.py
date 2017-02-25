import wiringpi as pi
import time

SW_PIN = 15

pi.wiringPiSetupGpio()
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_DOWN)

def rising():
    print("rising")
def falling():
    print("falling")
def both():
    print("both")
def setup():
    print("setup")

def counter(x):
    y = [x]
    def count():
        z = y[0]
        y[0] += 1
        return z
    return count

def counter3(x):
    y = x
    def count():
        nonlocal y
        z = y
        y += 1
        return z
    return count



while True:
    pi.wiringPiISR(SW_PIN, pi.INT_EDGE_RISING, rising)
    # pi.wiringPiISR(SW_PIN, pi.INT_EDGE_FALLING, falling)
    # pi.wiringPiISR(SW_PIN, pi.INT_EDGE_BOTH, both)
    # pi.wiringPiISR(SW_PIN, pi.INT_EDGE_SETUP, setup)
    time.sleep(1000)

