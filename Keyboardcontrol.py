import keyboard
import serial
import time

ser = serial.Serial('COM3', 9600, timeout = 1, write_timeout=1)

def main():
    while True:
        serial.Serial.flush(ser)
        serial.Serial.flushOutput(ser)
        Keyboard()
        serial.Serial.flushInput(ser)
        Received()

def Keyboard():
    if(keyboard.is_pressed('w')):
        ser.write('w'.encode())
    elif (keyboard.is_pressed('s')):
        ser.write('s'.encode())
    elif (keyboard.is_pressed('a')):
        ser.write('a'.encode())    
    elif (keyboard.is_pressed('d')):
        ser.write('d'.encode())
    time.sleep(0.05)

def Received():
    data = ser.read_until()
    decode_data = data.decode()
    sensor = decode_data.split()
    print(sensor[0],sensor[1])
    sensor = []
    time.sleep(0.04)

if __name__ == '__main__':
    main()