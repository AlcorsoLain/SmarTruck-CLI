from flask import *
from Blueprints.mainBL import main_Blueprint

class WebServer:
    _WebServerInst = None

    def __new__(cls):
        if not cls._WebServerInst:
            cls._WebServerInst = super(WebServer,cls).__new__(cls)
            return cls._WebServerInst
        
    def __init__(self) -> None:
        self.WebServer = Flask(__name__)
    
    def startServer(self,IP = '0.0.0.0', PORT = None) -> None:
        self.WebServer.run(host=IP)