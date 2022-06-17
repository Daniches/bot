import requests
from bs4 import BeautifulSoup
from modules.base_module import BaseModule

class GenerateHolliday(BaseModule):
    def run(self, update, context):
        response = requests.get(url='https://my-calend.ru/holidays', headers=[])
        soup = BeautifulSoup(response.content,'html.parser')
        hollidays = soup.find_all('li')
        holli_1=hollidays[44].find('a').text
        holli_url=hollidays[44].find('a').attrs['href']
        
        self.send(update, context, "Сегодня: "+ holli_1 + ' '+ holli_url)

public_holiday_module = GenerateHolliday()
