import configparser
from bot import Bot

#from modules.image_classificator.module import object_detection_module
from modules.advice_generator.module import generate_advice_module
from modules.news.module import generate_news_module
from modules.password_generator.module import generate_password_module
from modules.what_eat.module import chose_food_module
from modules.hackernews.module import hackernews_module
from modules.vacancies.module import random_vacancy_module
#from modules.film_generator.module import generate_film_module

config = configparser.ConfigParser()
config.read('config.ini')
token = config['TEST']['TOKEN']

bot = Bot(token)

bot.register(generate_password_module, ['Пароль', 'пароль', 'password'], "А если напишешь мне 'пароль' - я создам новый пароль!")
#bot.register(object_detection_module, ['Пароль', 'пароль', 'password'], "А если пришлешь мне фото - я найду на объекты!", module_type='image')
bot.register(generate_advice_module, ['Дай совет','Что посоветуешь','совет'], "А если напишешь мне 'совет' - я дам совет!")
bot.register(chose_food_module, ['Что поесть',"Что выбрать поесть","еда","есть","поесть","что выбрать"], "А если напишешь мне 'еда' - я дам совет по еде!")
bot.register(hackernews_module, ['hackernews',"news","новости","какие новости","что нового"], "А если напишешь мне 'hackernews' - я расскажу тебе новости!")
bot.register(random_vacancy_module, ['Вакансия','Вакансии','Вакансии Курск', 'вакансия'], "А если напишешь мне 'вакансия' - я постараюсь найти вакансию твоей мечты в Норбит!")
bot.register(generate_news_module, ['Новость','новость','новости', 'Новости'], "А если напишешь мне 'новость' - я расскажу тебе последнюю новость в России!")
#bot.register(generate_film_module, ['Фильм','фильм','Кино', 'Фильмы'], "А если напишешь мне 'фильм' - я предложу тебе фильм!")

bot.run()




