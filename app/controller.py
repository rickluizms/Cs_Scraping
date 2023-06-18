
from .core.scrap import Scrap
from .core.parser import Parser




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
        print(transf_data, '============ WORKS! ============')
        return