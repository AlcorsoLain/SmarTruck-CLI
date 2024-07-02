import serial
class ArduinoComm(object):
    def __new__(cls,port):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ArduinoComm,cls).__new__(cls)
        return cls.instance
    
    def __init__(self,commPort) -> None:
        try:
            self.ArduinoComm = serial.Serial(port=commPort, baudrate=115200, timeout=.1)
            print("Se ha abierto el puerto "+commPort)
        except:
            print("Ha pasado un problema al intentar abrir la comunicacion")

    
    def writeComm(self,msg):
        self.ArduinoComm.write(msg)

    def readRAWStr(self):
        while True:
            tempData = self.ArduinoComm.readline().decode().strip()
            if tempData:
                return tempData
            
    def readRAWChar(self):
        while True:
            tempChar = self.ArduinoComm.read()
            if tempChar:
                return tempChar
            

    def checkStatus(self):
        self.writeComm("?")
        status = self.readRAWChar()
        if status == '1':
            return "Todo bien"

    def readINTValue(self) -> int:
        TryInt = self.readRAWValue()
        try:
            return int(TryInt)
        except ValueError:
            raise Exception("El valor no pudo ser convertido a entero "+ValueError)