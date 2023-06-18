from .core.scrap import Scrap
from .core.parser import Parser
from .services.services import Services



class Controller:

    def __init__(self, src):
        self.url = src['url']
        self.type = src['type']
        self.endpoints = src['endpoints']
        
    def Extract(self):
        scrap = Scrap(self.url, self.type)
        data = scrap.get()
        return data

    def Transform(self, data):
        parser = Parser(self.type)
        transf_data = parser.Run(data)
        return transf_data
    
    def Load(self, transf_data):
        client = Services(self.endpoints)
        client.load(transf_data)
        return 'success'