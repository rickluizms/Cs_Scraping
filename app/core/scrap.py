from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from ..tools.parser import Parser


class Scrap:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Adicione essa linha para executar o Chrome em modo headless
        self.driver = webdriver.Chrome(options=self.options)
        self.parser = Parser()