
from .core.scrap import Scrap
from .core.parser import Parser



class Controller:

    def __init__(self):
        self.scraping = Scrap()
        self.parser = Parser()

    def Extract(self):
        scrap = self.scraping
        data = scrap.get()
        return data

    def Trasnform(self, data):

        return 
    
    def Load(self, transf_data):
        
        return