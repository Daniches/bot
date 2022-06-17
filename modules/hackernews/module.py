import requests
from bs4 import BeautifulSoup
from modules.base_module import BaseModule

class Hackernews(BaseModule):

    @staticmethod
    def fetch_news_data():
        r = requests.get('https://news.ycombinator.com/')       
        soup = BeautifulSoup(r.text, features="html.parser")
        titles = soup.select('tr.athing > .title > a')
        attrs = soup.select('tr.athing ~ tr > .subtext')
    
        data = []
        for title, attr in zip(titles, attrs):
            data.append({
                'href': title['href'],
                'title': title.text,
                'info': attr.text.strip().split('|')[0]
            })
        return data

    def run(self, update, context):
        try:
            news = Hackernews.fetch_news_data()

            message_text = (
                '<b>Топ 5 новостей с hackernews</b>\n'
                '<i>'+'-'*50+'</i>\n'
            )

            for i, item in enumerate(news[:5]):
                href, title, info = item['href'], item['title'], item['info']
                text = (
                    f'<b>{i+1}. <a href="{href}">{title}</a></b>\n'
                    f'<i>{info}</i>\n\n'
                )
                message_text += text
            
            context.bot.send_message(chat_id=update.effective_chat.id,
                                  text=message_text,
                                  parse_mode='HTML')
        except Exception as e:
            self.send(update, context, text="Что-то пошло не так, попробуй позже (")


hackernews_module = Hackernews()
