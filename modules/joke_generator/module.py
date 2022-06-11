import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from modules.base_module import BaseModule

class Joke_generator(BaseModule):
    def __init__(self):
        pass

    def run(self, update, context):
        page_link = f'https://www.anekdot.ru/random/anekdot/'
        response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
        html = response.content
        soup = BeautifulSoup(html,'html.parser')
        obj = soup.find('div', attrs = {'class':'text'})

        self.send(update, context, obj.text)

joke_generator_module = Joke_generator()