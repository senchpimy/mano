import serial

SerialObj = serial.Serial('/dev/ttyACM0')
while True:
    SerialObj.write(input("Ingrese").encode('UTF-8'))
