import time
import sys
import RPi.GPIO as GPIO

up = 'up'
up_1 = '101011100110111011011110101001000111111101111111111110100110110000'
up_2 = '101011100110111011011110101001000111111101111111111011011101111110'

down = 'down'
down_1 = '101011100110111011011110101001000111111101111111110111100101000000'
down_2 = '101011100110111011011110101001000111111101111111111011011101111110'

stop = 'stop'
stop_1 = '101011100110111011011110101001000111111101111111111011100110000000'

pause = 0.5
short_delay = 0.00018
long_delay = 0.00058
extended_delay = 0.00518
half_code_delay = 0.01033

NUM_ATTEMPTS = 4
TRANSMIT_PIN = 23
print "var settings done"

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    print "entering code"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(pause)
    # UP COMMAND
    if code is up or code == 100:
        print "going up"
        for t in range(NUM_ATTEMPTS):
            print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            for i in up_1:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_delay)
                    print "  1 sent"
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_delay)
                    print "  0 sent"
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(extended_delay)
            print "  extended delay sent"
        print "out of for loop up_1"
        time.sleep(half_code_delay)
        print "adding half code delay"
        for t in range(NUM_ATTEMPTS):
            print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            for i in up_2:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_delay)
                    print "  1 sent"
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_delay)
                    print "  0 sent"
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(extended_delay)
            print "  extended delay sent"
        print "out of for loop up_2"
        print "out of if up"
    # END UP COMMAND

    # DOWN COMMAND
    if code is down or code == 0:
        print "going down"
        for t in range(NUM_ATTEMPTS):
            print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            for i in down_1:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_delay)
                    print "  1 sent"
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_delay)
                    print "  0 sent"
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(extended_delay)
            print "  extended delay sent"
        print "out of for loop down_1"
        time.sleep(half_code_delay)
        print "adding half code delay"
        for t in range(NUM_ATTEMPTS):
            print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            for i in down_2:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_delay)
                    print "  1 sent"
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_delay)
                    print "  0 sent"
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(extended_delay)
            print "  extended delay sent"
        print "out of for loop down_2"
        print "out of if down"
    # END DOWN COMMAND

    # STOP COMMAND
    if code is stop or code < 100 or code > 0:
        print "stopping"
        for t in range(NUM_ATTEMPTS):
            print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            for i in stop_1:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_delay)
                    print "  1 sent"
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_delay)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_delay)
                    print "  0 sent"
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(extended_delay)
            print "  extended delay sent"
        print "out of for loop stop_1"
        # time.sleep(half_code_delay)
        # print "adding half code delay"
        # for t in range(NUM_ATTEMPTS):
        #     print "entering for %s on %s" % (t, NUM_ATTEMPTS)
        #     GPIO.output(TRANSMIT_PIN, 1)
        #     time.sleep(extended_delay)
        #     for i in stop_2:
        #         if i == '1':
        #             GPIO.output(TRANSMIT_PIN, 1)
        #             time.sleep(short_delay)
        #             GPIO.output(TRANSMIT_PIN, 0)
        #             time.sleep(long_delay)
        #             print "  1 sent"
        #         elif i == '0':
        #             GPIO.output(TRANSMIT_PIN, 1)
        #             time.sleep(long_delay)
        #             GPIO.output(TRANSMIT_PIN, 0)
        #             time.sleep(short_delay)
        #             print "  0 sent"
        #         else:
        #             continue
        #     GPIO.output(TRANSMIT_PIN, 0)
        #     time.sleep(extended_delay)
        #     print "  extended delay sent"
        # print "out of for loop stop_2"
        print "out of if stop"
    # END STOP COMMAND

    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(half_code_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

