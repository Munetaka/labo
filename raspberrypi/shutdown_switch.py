import wiringpi as pi
import time
import subprocess

SW_PIN = 15

pi.wiringPiSetupGpio()
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_DOWN)


def timer():
    start = time.time()
    print('init time')
    print('start', start)
    def diff():
        nonlocal start
        return time.time() - start
    return diff


prevtime = {}
def check_chattering(timekey):
    global prevtime
    if prevtime.get(timekey) == None:
        prevtime[timekey] = time.time() - 10
    currenttime = time.time()
    diff = currenttime - prevtime[timekey]
    prevtime[timekey] = currenttime

    if diff <= 0.01:
        return False
    else:
        return True

def shutdown():
    print("shutdown")
    cmd = 'sudo shutdown now'
    subprocess.call(cmd.split(" "))
    exit()

def reboot():
    print("reboot")
    cmd = 'sudo shutdown -r now'
    subprocess.call(cmd.split(" "))
    exit()

state = False
timekeeper = None
def switch_trigger():
    if check_chattering("switch") == False:
        return

    global state
    global timekeeper
    if state:
        diff = timekeeper()
        state = False
        print('pulled up: ', diff, 'sec')
        if 3 <= diff:
            shutdown()
        elif 1 <= diff:
            reboot()
    else:
        timekeeper = timer()
        state = True
        print('pulled down')


while True:
    pi.wiringPiISR(SW_PIN, pi.INT_EDGE_BOTH, switch_trigger)
    time.sleep(1000)
