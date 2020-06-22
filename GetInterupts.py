import RPi.GPIO as GPIO
import spidev
import time
import sys
from Tkinter import *


# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #set resister to up?
#GPIO.add_event_detect(12, GPIO.RISING)

spi = spidev.SpiDev() 
spi.open(0, 0)

timesup = 10
c = 0
channel = 0
T = timesup
#print c
def read_wind_dir(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

##count interupts for given amount of time
def main():
    timenow = time.time()
    c = 0
    while time.time() < timenow  + timesup: #look for and count pulses for <timesup> seconds
        #print 'In It'
        #print GPIO.input(18)
        if GPIO.input(13) <> 1: 
            c = c + 1
            print 'pluse ', c
              
    windspeed = c * (2.25/T) #calculate wind speed based on no. of pulses, time and Davis specific factor 
    #get wind direction via aenomometer pot voltage 
    #reading = read_wind_dir(0)
    #voltage = reading * 3.3 / 1024
    #winddir = (voltage / 3.3) * 360
    #while True:
    #Read all the ADC channel values in a list.
    #values = [0]*8
    #for i in range(8):
    # The read_adc function will get the value of the specified channel (0-7).
    #values[i] = mcp.read_adc(i)
    value = mcp.read_adc(0)
    voltage = value * 3.3 / 1024
    winddir = (voltage / 3.3) * 360
    print 'Value ' + str(value) + ' Voltage ' + str(voltage)
        
    print windspeed, winddir
    
    GPIO.cleanup()   
    
    
master = Tk()

Label(master, text=windspeed).grid(row=0, column=0)
mainloop()

#for testing
#for c in range(1, 1000):
    #c += 1
    
#windspeed = c*(2.25/T)
#print windspeed

if __name__ == "__main__":
    sys.exit(main())
