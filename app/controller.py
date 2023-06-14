from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from .core.scrap import Scrap
from .tools.parser import Parser



class Controller:

    def __init__(self, connection):
        self.scrapping = Scrap()
        self.parser = Parser()
        self.connection = connection

    def Extract(self):
        scrapping = self.scrapping

        ML_Offers = scrapping.MLScrap()
        Magalu_Offers = scrapping.MagaluScrap()

        data = {
            'ML_offers': ML_Offers,
            'Magalu_offers': Magalu_Offers,
        }

        return data

    def Trasnform(self, data):
        parser = self.parser 

        ML_html = data['ML_offers']
        Magalu_html = data['Magalu_offers']

        df_ML = parser.ParseRaw_ML(ML_html)
        df_Magalu = parser.ParseRaw_Magalu(Magalu_html)

        transf_data = {
            'df_ML': df_ML,
            'df_Magalu': df_Magalu
        }

        return transf_data
    
    def Load(self, transf_data):
        connection = self.connection

        return