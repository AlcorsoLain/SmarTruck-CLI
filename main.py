from Utilities.webUtilities import *
from Utilities.sysUtilities import *
from SerialDriver.main import ArduinoComm
from Forms.Forms import MainWindow
from threading import Thread
import sys

_ArduinoComm = None
_webApp = None
_GUIApp = None


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print(mensajeAyuda)
    else:
        for index,arg in enumerate(args):
            match arg:
                case '-p':
                    print("Conectado al puerto "+args[index+1])
                    _ArduinoComm = ArduinoComm(args[index+1])

                case '-h' | '--help' | '-H':
                    print(mensajeAyuda)
                    #
                case '-s' | '--server' | '-S':
                    print("Iniciando servidor")
                    _webApp = WebServer()
                    Thread(target= _webApp.startServer).start()

                case '-g' | '--gui' | '-G':
                    if len(args) > 1:
                        print("Error, solo se puede lanzar GUI sin otros argumentos")
                    else:
                        print("Iniciando GUI")
                        _webApp = MainWindow()
                        _webApp.mainloop()
                case _:
                    if arg[0] == '-':
                        print("Inserte un comando valido")

if __name__ == '__main__':
    main()