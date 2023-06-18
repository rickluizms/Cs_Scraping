from bs4 import BeautifulSoup
import pandas as pd
import json

class Parser:

    def __init__(self, type):
        self.type = type

    def Run(self, html_content):
        type = self.type

        if type == '1':
            transf_data = Parser.Nesha(html_content)

        if type == '2':
            transf_data = ""

        if type == '3':
            transf_data = ""

        return transf_data
    
    def Nesha(data):
        transf_data = {}
        for html_content in data:
            try:
                soup = BeautifulSoup(html_content, 'html.parser')
                images = soup.select('.card-header img')

                # Nome e Imagem
                for image in images:
                    skin_name = image.get('alt')
                    skin_img_src = image.get('src')
                    
                # Disponibilidade
                dispon = soup.find('span', class_="badge")
                if dispon:
                    skin_dispon = dispon.getText()

                # Fase
                phase = soup.find('span', class_="phase")
                if phase:
                    skin_fase = phase.getText()
                else:
                    skin_fase = 'NoNe'
                
                # Preço anterior
                old_price = soup.find('p', class_="text-danger")
                if old_price:
                    skin_old_price = old_price.getText()
                else:
                    skin_old_price = 'NoNe'

                # Preço
                price = soup.find('p', class_="font-weight-normal")
                if price:
                    skin_price = price.getText()
                else:
                    skin_price = 'NoNe'

                # Valor do Desconto
                disc = soup.find('span', class_="font-weight-bold")
                if disc:
                    skin_disc = disc.getText()
                else:
                    skin_disc = 'NoNe'

                # Float
                fn = soup.find('span', class_="text-muted")
                if fn:
                    skin_fn = fn.getText()
                else:
                    skin_fn = 'NoNe'
                
                skin = {
                    'nome': skin_name,
                    'img': skin_img_src,
                    'dispon': skin_dispon,
                    'fase': skin_fase,
                    'old_price': skin_old_price,
                    'price': skin_price,
                    'discount': skin_disc,
                    'fn': skin_fn,
                }

                transf_data[skin_name] = skin

            except AttributeError as e:
                print(f"Erro ao extrair dados: {e}")

        return transf_data

    