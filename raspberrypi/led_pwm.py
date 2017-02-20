import time, wiringpi as pi

led_pin = 14

pi.wiringPiSetupGpio()
pi.pinMode( led_pin, pi.OUTPUT )

pi.softPwmCreate( led_pin, 0, 100)
pi.softPwmWrite( led_pin, 0 )

while True:
    strong = 0
    while ( strong <= 100 ):
        pi.softPwmWrite( led_pin, strong )
        time.sleep(0.1)
        strong = strong + 1

    pi.softPwmWrite( led_pin, 0 )
    time.sleep(2)

