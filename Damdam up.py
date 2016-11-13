import time
import sys
import RPi.GPIO as GPIO

up_1 = '101011100110111011011110101001000111111101111111111110100110110000'
up_2 = '101011100110111011011110101001000111111101111111111011011101111110'

pause = 0.5
short_delay = 0.00018
long_delay = 0.00058
extended_delay = 0.00518
half_code_delay = 0.01033

NUM_ATTEMPTS = 4
TRANSMIT_PIN = 23
print "var settings"

def transmit_code():
    '''Transmit a chosen code string using the GPIO transmitter'''
    print "enter code"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(pause)
    for t in range(NUM_ATTEMPTS):
        if t == '1':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
        else:
            continue
        for i in up_1:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(half_code_delay)
    for t in range(NUM_ATTEMPTS):
        if t == '1':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
        else:
             continue
        for i in up_2:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(half_code_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')