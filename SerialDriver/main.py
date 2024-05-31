import serial

class ArduinoComm:
    _arduino = None

    def __new__(cls):
        if not cls._arduino:
            cls._arduino = super(ArduinoComm,cls).__new__(cls)
            return cls._arduino
        
    def __init__(self,commPort) -> None:
        self.ArduinoComm = serial.Serial(port=commPort, baudrate=115200, timeout=.1)
        print("Se ha abierto el puerto "+commPort)
    
    def writeComm(self,msg):
        self.ArduinoComm.write(msg)