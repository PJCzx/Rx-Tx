import time
import sys
import RPi.GPIO as GPIO

a_on = '1111111111111010101011101'
a_off = '1111111111111010101010111'
b_on = '1111111111101110101011101'
b_off = '1111111111101110101010111'
c_on = '1111111111101011101011101'
c_off = '1111111111101011101010111'
d_on = '1111111111101010111011101'
d_off = '1111111111101010111010111'
short_delay = 0.00045
long_delay = 0.00090
extended_delay = 0.0096

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 12

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
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
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

