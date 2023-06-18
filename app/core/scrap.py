from selenium import webdriver
import time



class Scrap:

    def __init__(self, url, type):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Adicione essa linha para executar o Chrome em modo headless
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url
        self.type = type

    def get(self):

        if self.type == '1':
            data = Scrap.Nesha(self)
        if self.type == '2':
            return
        if self.type == '3':
            return
        if self.type == '4':
            return

        return data
        
    def Nesha(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(12)

        elements = driver.find_elements("css selector", '.card') # Filtrar todos os elementos com a classe "card"
        data = []

        for index, element in enumerate(elements, start=1):
            data.append(element.get_attribute('outerHTML'))

            # Verificar se o índice atual é divisível por 4
            if index % 3 == 0:
                # Realizar um pequeno scroll na página
                driver.execute_script("window.scrollBy(0, 300);")
                time.sleep(2)  # Aguardar um tempo para o conteúdo carregar

        return data

        