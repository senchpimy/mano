import serial




class hand():
    def __init__(self):
        self.ard = serial.Serial('/dev/ttyACM0',9600)
        #ard = serial.Serial('COM3', 9600)
    def thumb(self, num:int):
        nu = str(num)
        st = f"T{nu.zfill(3)}\n"
        self.ard.write(st.encode('UTF-8'))
    def index(self, num:int):
        nu = str(num)
        st = f"I{nu.zfill(3)}\n"
        self.ard.write(st.encode('UTF-8'))
    def middle(self, num:int):
        nu = str(num)
        st = f"M{nu.zfill(3)}\n"
        self.ard.write(st.encode('UTF-8'))
    def ring(self, num:int):
        nu = str(num)
        st = f"R{nu.zfill(3)}\n"
        self.ard.write(st.encode('UTF-8'))
    def pinky(self, num:int):
        nu = str(num)
        st = f"P{nu.zfill(3)}\n"
        self.ard.write(st.encode('UTF-8'))
    def close(self):
        self.ard.close()
