import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #set resister to up?
GPIO.add_event_detect(20, GPIO.RISING, bouncetime = 200)
timesup = 10

def main():
    timenow = time.time()
    c = 0
    while time.time() < timenow  + timesup: #look for and count pulses for <timesup> seconds
        #print GPIO.input(20)
        #print GPIO.input(18)
        #if GPIO.input(20) <> 0:
        if GPIO.event_detected(20):
            c = c + 1
            print 'pluse ', c
    print c
              
    GPIO.cleanup()   
    
    

#for testing
#for c in range(1, 1000):
    #c += 1
    
#windspeed = c*(2.25/T)
#print windspeed

if __name__ == "__main__":
    sys.exit(main())
