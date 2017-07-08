import time
import sys
import RPi.GPIO as GPIO

# UP contains 8 bursts 4*up1 then 4*up2

percent = 0.75
THIGH =     0.000220*percent
TSHORT =    0.000350*percent
TLONG =     0.001400*percent
cleaning_delay = 0.002675*percent
ending_delay =   0.010600*percent

NUM_ATTEMPTS = 4
TRANSMIT_PIN = 23

def encode(code):
    for i in code:
        if i == '1':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(THIGH)
         
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TLONG)
         
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(THIGH)
         
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TSHORT)
        
        elif i == '0':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(THIGH)
         
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TSHORT)
         
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(THIGH)
         
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TLONG)

        else:
            continue

def transmit_code(code, buttonId):
    '''Transmit a chosen code string using the GPIO transmitter'''
    print code
    print buttonId
    #buttonId can bo between 1 and 70
    myCode = 1067894928 + buttonId
    print myCode

    on = '00' + bin(myCode)[2:]#'00111111101001101100100010010000'
    off = '00' + bin(myCode - 16)[2:]#'00111111101001101100100010000000'

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)

    for t in range(NUM_ATTEMPTS):

        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(THIGH)

        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(cleaning_delay)

        if code is on or code == 1 or code == 100:
            encode(on)

        if code is off or code == 0:
            encode(off)

        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(THIGH)

        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(ending_delay)

        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(THIGH)
    
    GPIO.cleanup()

if __name__ == '__main__':
    code = sys.argv[1]
    buttonId = '1'
    if len(sys.argv) >= 3: buttonId = sys.argv[2] 
    print "sending code: " + code + " to buttonId: " + buttonId

    exec('transmit_code(' + str(code) + ',' +  str(buttonId) + ')')
