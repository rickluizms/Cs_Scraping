from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from .core.scrap import Scrap
from .core.parser import Parser



class Controller:

    def __init__(self, connection):
        self.scrapping = Scrap()
        self.parser = Parser()
        self.connection = connection

    def Extract(self):

        return 

    def Trasnform(self, data):

        return 
    
    def Load(self, transf_data):
        connection = self.connection

        return