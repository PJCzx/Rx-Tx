import time
import sys
import RPi.GPIO as GPIO

up1 = '101011100110110000100001010111100111111101111111111110100110011000'
up2 = '101011100110110000100001010111100111111101111111111011011101100110'

short_delay = 0.000185
long_delay = 0.000600
mid_delay = 0.0052
final_delay = 0.160

NUM_ATTEMPTS = 2
TRANSMIT_PIN = 12

def transmit_code():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)

    for t in range(NUM_ATTEMPTS):
        for i in up1:
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
    time.sleep(mid_delay)
    for t in range(NUM_ATTEMPTS):
        for i in up2:
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
    time.sleep(final_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')