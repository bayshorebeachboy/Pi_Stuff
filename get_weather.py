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


def read_wind_dir(channel):
    value = mcp.read_adc(0)
    voltage = value * 3.3 / 1024
    winddir = (voltage / 3.3) * 360
    #r = spi.xfer2([1, (8 + channel) << 4, 0])
    #adc_out = ((r[1]&3) << 8) + r[2]
    print value, voltage
    return winddir

def read_windspeed():
    timesup = 5
    c = 0
    T = timesup
    timenow = time.time()
    while time.time() < timenow  + timesup: #look for and count pulses for <timesup> seconds
        if GPIO.input(13) <> 1: 
            c = c + 1
            print 'pluse ', c
              
    windspeed = c * (2.25/T) #calculate wind speed based on no. of pulses, time and Davis specific factor 

    #print 'Value ' + str(value) + ' Voltage ' + str(voltage)      
    print windspeed
    return windspeed

def main():
    while True:
        ws = read_windspeed()
        wd = read_wind_dir(0)
        wind = "Speed = " + str(round(ws, 2)) + "   Dir. = " + str(round(wd, 2))
        w.set(wind)
        master.update_idletasks()
        #print ws, wd

master = Tk()
w = StringVar()
master.title("Wind Data")

Label(master, textvariable=w).grid(row=0, column=0)
Button(master, text="Quit", command=master.quit).grid(row=1, column=0)
main()
mainloop()

#if __name__ == "__main__":
#    sys.exit(main())
GPIO.cleanup()   
