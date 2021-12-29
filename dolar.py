import requests

class DollarValue():
    """Classe retorna valor do dolar de uma api pública -> AwesomeAPI"""

    def __init__(self):
        self.value = -1

    def consult(self):
        url = "https://economia.awesomeapi.com.br/json/all/USD"
        r = requests.get(url)
        if (r.status_code == 200):
            json_parsed = r.json()
            self.value = json_parsed['USD']['high']
        else:
            self.value = -1




        
