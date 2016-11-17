import time
import sys
import RPi.GPIO as GPIO

# UP contains 8 bursts 4*up1 then 4*up2
up = 'up'
up_1 = '101011100110110000100001010111100111111101111111111110100110011000'
up_2 = '101011100110110000100001010111100111111101111111111011011101100110'

down = 'down'
down_1 = '101011100110111011011110101001000111111101111111110111100101000000'
down_2 = '101011100110111011011110101001000111111101111111111011011101111110'

stop = 'stop'
stop_1 = '101011100110111011011110101001000111111101111111111011100110000000'

short_delay =    0.000140
long_delay =     0.000540
extended_delay = 0.005400

cleaning_delay = 0.5

NUM_ATTEMPTS = 4
TRANSMIT_PIN = 23

def encode(code):
    for i in code:
        if i == '1':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(short_delay)
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(long_delay)
            #print "  1 sent"
        elif i == '0':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(long_delay)
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(short_delay)
            #print "  0 sent"
        else:
            continue

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    #print "entering code"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)

    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(cleaning_delay)

    # UP COMMAND
    if code is up or code == 100:
        #print "going up"
        for t in range(NUM_ATTEMPTS):
            #print "entering for %s on %s" % (t, NUM_ATTEMPTS)

            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)

            encode(up_1)

        for t in range(NUM_ATTEMPTS):
            #print "entering for %s on %s" % (t, NUM_ATTEMPTS)

            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)

            encode(up_2)

    # END UP COMMAND

    # DOWN COMMAND
    if code is down or code == 0:
        #print "going down"
        for t in range(NUM_ATTEMPTS):
            #print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)

            encode(down_1)

        for t in range(NUM_ATTEMPTS):
            #print "entering for %s on %s" % (t, NUM_ATTEMPTS)
            
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            
            encode(down_2)

    # END DOWN COMMAND

    # STOP COMMAND
    if code is stop or (code < 100 and code > 0):
        #print "stopping"

        for t in range(NUM_ATTEMPTS):
            #print "entering for %s on %s" % (t, NUM_ATTEMPTS)

            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(extended_delay)
            
            encode(stop_1)

    # END STOP COMMAND

    GPIO.output(TRANSMIT_PIN, 0)
    time.sleep(cleaning_delay)
    
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
