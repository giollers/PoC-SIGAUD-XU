from Adafruit_IO import *
import RPi.GPIO as GPIO
import serial

aio = Client('giollers','aio_EQnq51ltfn5sEhP7N3chUJ31IyE9')
while True:
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.flush()        
        if ser.in_waiting >= 0:
        	temp = ser.readline().decode('utf-8').rstrip()            
        aio.send("data",temp)
 
    if int(aio.receive('control').value)==1:
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(24, GPIO.HIGH)
           
    else:
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(24, GPIO.LOW)
