import requests
import json

class Services:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def load(self, datas):
        endpoint = self.endpoint

        for data in datas.values():

            url = (f'http://localhost:8080{endpoint}')
            json_data = json.dumps(data)
            headers = {'Content-type': 'application/json'}

            response = requests.post(url, data=json_data, headers=headers)

            if response.status_code == 200:
                print("Arquivo JSON enviado com sucesso!")
            else:
                print("Falha ao enviar o arquivo JSON. Código de resposta:", response.status_code)

        
        return