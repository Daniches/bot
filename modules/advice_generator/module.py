import requests
from bs4 import BeautifulSoup
from modules.base_module import BaseModule


class GenerateAdvice(BaseModule):
    def run(self, update, context):
        resp = requests.get(url='http://old.randomes.top/sovet.php', headers=[])
        advice = (BeautifulSoup(resp.text).
                    find('div', {'id': 'main'}).
                    find('span').
                    text)

        self.send(update, context, "🔮 "+advice)


generate_advice_module = GenerateAdvice()
