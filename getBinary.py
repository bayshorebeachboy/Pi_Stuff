     #getbinary

import RPi.GPIO as GPIO

number = 145 
#number = int(raw_input("Enter a Number < 255: "))
def getBin(number):
    bine = []
    while number > 0:
        divide = number/2
        mod = number%2
        number = divide
        bine.append(mod)
    return(bine)
#GPIO.cleanup()         
#print "Enter 0 to Quit"

while number <> 0: 
    number = int(raw_input("Enter a Number < 255 or 0 to Quit: "))
    if number <> 0: 
        backwards = getBin(number)
        converted = ''
        for i in reversed(backwards):
            converted = converted + str(i)
        for i in range(0, 8 - len(converted)):
            converted = str(0) + converted
        print converted
        
        #pin mappings
        #position 7  = 0 0*2^7      GPIO pin - 14
        #position 6  = 1 1*2^6 = 64 GPIO pin - 15
        #position 5  = 1 1*2^5 = 32 GPIO pin - 18
        #position 4  = 1 1*2^4 = 16 GPIO pin - 23
        #position 3  = 0 0*2^3	    GPIO pin - 24
        #position 2  = 0 0*2^2	    GPIO pin - 25
        #position 1  = 0 0*2^1	    GPIO pin - 12
        #position 0  = 0 0*2^0	    GPIO pin - 16
                                          # = 112
               
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)
        
        print '--------------------'
        
        pins = ['14', '15', '18', '23', '24', '25', '12', '16']
        i = 0
        for pin in pins:
            #print 'pin ', pin, ' = ' + converted[i]
            setpin = 'GPIO.output(' + pin +', ' + converted[i] + ')'
            eval(setpin)
            print setpin
            i = i + 1
GPIO.cleanup()
