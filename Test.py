import serial

import time
import math

ser = serial.Serial('COM3', 9600, timeout = 1, write_timeout=1)
time.sleep(0.4)
out1 = "sensor 1"

while True:
    data = ser.read_until()
    data = data.decode()
    sensor = data.split()
    sensor1 = sensor[0]
    sensor2 = sensor[1]
    print(sensor1," ",sensor2)
    time.sleep(0.01)


    
    #sensor = data.spit()
    #print(sensor[0])
    #print(sensor[1]) 