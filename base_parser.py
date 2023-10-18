import requests
import json
from confix import *



# основной парсер

class BaseParser:
    def __init__(self):
        self.url = URL
        self.host = HOST

    def get_html(self, link):
        response = requests.get(link)
        try:
            return response.text
        except requests.HTTPError:
            print(f'Произошла ошибка {response.status_code}')

    @staticmethod
    def save_date_to_json(path, date):
        with open(f'{path}.json', mode='w', encoding='UTF-8') as file:
            json.dump(date, file, ensure_ascii=False, indent=4)




