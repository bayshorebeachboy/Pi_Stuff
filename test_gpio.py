import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(14, GPIO.OUT)           # set GPIO24 as an output   

try:  
    while True:  
        GPIO.output(14, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(1
              )
        print 'high'                # wait half a second  
        GPIO.output(14, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(1)
        print 'low'                    

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
