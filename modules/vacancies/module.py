import requests
from random import choice
from bs4 import BeautifulSoup
from modules.base_module import BaseModule


class RandomVacancy(BaseModule):

    @staticmethod
    def get_random_vacancy():

        link = "https://www.norbit.ru/karera/vakansii/kursk/"
        site = "https://www.norbit.ru"
        departaments = ['departament-crm-kursk/',
                    'departament-hr-krsk/',
                    'vakansii-departamenta-microsoft-dynamics-ax-kursk/',
                    'departament-nbt-srm-krsk/',
                    'departament-lanit-omni-krsk/',
                    'departament-mashinnogo-obucheniya/',
                    'departament-obespecheniya-krsk/',
                    'departament-upravlencheskogo-konsaltinga/',
                    'otdel-administrativnogo-upravleniya-kursk/']

        vacancies = []

        #Проходимся по всем департаментам на сайте
        for departament in departaments:
            soup = BeautifulSoup(requests.get(link + departament).text, 'html.parser')

            #Находим все публикации о вакансиях и собираем информацию о них в список
            publications = soup.find_all('a', class_="title customfont")
            for publication in publications:
                image_href = site + publication.find('img')['src']
                text = publication.text.strip()
                href = site + publication['href']
                vacancies.append({'img':image_href, 'text':text, 'link':href})
        return (choice(vacancies))

    def run(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Секундочку, ищу вакансию твоей мечты!☺️")
        try:
            vacancy = RandomVacancy.get_random_vacancy()
            message_text = '\n{0}\n<a href="{1}"><i>Cсылка на вакансию</i></a>'.format(vacancy['text'],vacancy['link'])

            context.bot.sendPhoto(chat_id=update.effective_chat.id,
                                  photo = vacancy['img'],
                                  caption=message_text,
                                  parse_mode='HTML')
        except:
            self.send(update, context, text="Прости, что-то пошло не так😥")


random_vacancy_module = RandomVacancy()
