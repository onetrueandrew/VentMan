import RPi.GPIO as GPIO
import time
import datetime
import csv

channel1 = 18 #hookup to relay1
channel2 = 23 #hookup to relay2
current_datetime = str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"))

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1, GPIO.OUT)
GPIO.setup(channel2, GPIO.OUT)

def HIGH(pin):
    GPIO.output(pin, GPIO.HIGH)

def LOW(pin):
    GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    try:
        #EXTEND TO CLOSE
        HIGH(channel1)
        LOW(channel2)
        time.sleep(0.5)
        GPIO.cleanup()
        open_log = [current_datetime,'opened']
        with open(r'/home/pi/dev/vent.log','a') as log:
                writer = csv.writer(log)
                writer.writerow(open_log)
    except KeyboardInterrupt:
        GPIO.cleanup()
