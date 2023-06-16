import serial
import time

ard = serial.Serial('COM3', 9600)

# ard.readline()
ard.write(b'a')
ard.close()
