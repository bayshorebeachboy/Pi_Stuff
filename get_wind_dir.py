import time
import sys

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from daemonize import Daemonize

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
pidfile = "/tmp/winddir.pid"



# Main program loop.
def main():
    while True:
        values = [0]*8
        value = mcp.read_adc(0)
        voltage = value * 3.3 / 1024
        print 'Value ' + str(value) + ' Voltage ' + str(voltage)
        winddir = (voltage /  3.3) * 360
        print "Dir: " + str(winddir)
        winddirlog = open("/tmp/winddirlog", "w+")
        writeme = str(winddir)
        winddirlog.write(writeme)
        winddirlog.write("\n")
        winddirlog.close()
        # Pause for half a second.
        time.sleep(0.5)

#if __name__ == "__main__":
#    sys.exit(main())

print "Start Daemon..."
wdd = Daemonize(app="/home/pi/Documents/python_files/get_wind_dir.py", pid = pidfile, action=main)
wdd.start()

