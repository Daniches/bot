from selenium import webdriver
from modules.base_module import BaseModule


class NicknameGenerator(BaseModule):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()
        self.driver.get('https://mindtnv.gitlab.io/deadinsidenickgenerator/')

    def run(self, update, context):
        self.driver.find_element(by='id', value='card-generate-button').click()
        nickname = self.driver.find_element(by='id', value='card-nickname').text

        self.send(update, context, nickname)


nickname_generator_module = NicknameGenerator()
