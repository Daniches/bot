from selenium import webdriver
from modules.base_module import BaseModule


class GenerateFilm(BaseModule):
    def __init__(self):
        pass

    def run(self, update, context):
        driver = webdriver.Firefox()
        driver.get("https://www.kinopoisk.ru/chance/")

        elem = driver.find_element_by_class_name("button").click()

        film = driver.find_element_by_class_name("filmName")
        film_text = film.find_element_by_tag_name("a")

        film_text = film_text.text

        span_text = film.find_element_by_tag_name("span")
        span_text = span_text.text

        driver.close()

        self.send(update, context, film_text+"\n"+span_text)


generate_film_module = GenerateFilm()
