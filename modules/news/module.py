import requests
from bs4 import BeautifulSoup
from modules.base_module import BaseModule


class GenerateNews(BaseModule):
    def run(self, update, context):
        resp = requests.get(url='https://ria.ru/location_rossiyskaya-federatsiya/', headers=[])
        advice = (BeautifulSoup(resp.text).
                    find('a', {'class': 'list-item__title color-font-hover-only'}).
                    text)
        url = (BeautifulSoup(resp.text).
                    find('a', {'class': 'list-item__title color-font-hover-only'}).
                    attrs["href"])

        self.send(update, context, "📰 "+ advice + ' ' + url)


generate_news_module = GenerateNews()