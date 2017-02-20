import wiringpi as pi

LED_PIN = 14
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.digitalWrite(LED_PIN, pi.LOW)
