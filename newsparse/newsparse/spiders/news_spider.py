# Импортируем модуль scrapy
import scrapy
import time
import sqlite3
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import yaml

# Импортируем модуль для округления в меньшую сторону
from math import floor
# Импортируем модуль получения даты
from dateparser import parse

#  Задаем имя конфигурационного источника через меню
site_choice = input(f'Выбери новостной сайт для парсинга: '
                    f'1-nur.kz; '
                    f'2-scientificrussia.ru; '
                    f'3-tengrinews.kz; '
                    f'4-mining.kz; '
                    f'0-Выход;'
                    f'__: ')
if site_choice == '0':
    quit()
elif site_choice == '1':
    yaml_file_name = 'nurkz_config.yaml'
elif site_choice == '2':
    yaml_file_name = 'scientificrussiaru_config.yaml'
elif site_choice == '3':
    yaml_file_name = 'tengrinewskz_config.yaml'
elif site_choice == '4':
    yaml_file_name = 'miningkz_config.yaml'
else:
    quit()

# # Задаем имя конфигурационного источника вручную
# yaml_file_name = 'miningkz_config.yaml'

# Считываем содержимое конфигурационного файла
with open((f'configs/{yaml_file_name}'), 'r') as file:
    set_a_ = yaml.load(file, Loader=yaml.FullLoader)

# Создаём класс паука и его методов
class NewsSpider(scrapy.Spider):
    name = 'news_spider'

    # Импортируем настройки паука
    start_urls = set_a_['start_urls']
    allowed_domains = set_a_['allowed_domains']
    max_depth = set_a_['max_depth']
    concurrent_requests = set_a_['concurrency']
    user_agent = set_a_['user_agent']


    def parse(self, response):
        depth = response.meta.get('depth', 0)  # текущая глубина
        # Если текущая глубина меньше или равна заданной глубине
        if depth <= self.max_depth:
            # Собираем все ссылки с текущей страницы
            links = response.css('a::attr(href)').getall()
            for link in links:
                if isinstance(link, str):
                    if '+7' not in link and 'mailto' not in link:
                        # Углубляемся
                        yield response.follow(link, callback=self.parse, meta={'depth': depth + 1})
        # Передаём ссылки уровня в анализатор структуры
        yield from self.parse_news(response)


    def parse_news(self, response):
        # Импорт структур для извлечения новости(мэссэджа)
        title_tag = set_a_['title_tag']
        title_class = set_a_['title_class']
        content_tag = set_a_['content_tag']
        content_class = set_a_['content_class']
        date_cut = set_a_['date_cut']

        # Получаем ссылку как атрибут объекта response, переданную  в генераторе функции parse
        link = response.url

        # Парсим заголовок новости
        if title_class:
            try:
                title = str(response.xpath(f'//{title_tag}[@class="{title_class}"]//text()').get()).strip()
            except:
                title = None
        else:
            try:
                title = str(response.xpath(f'//{title_tag}//text()').get()).strip()
            except:
                title = None

        #  Парсим содержание новости
        if content_class:
            try:
                content = ''.join(response.xpath(f'//{content_tag}[@class="{content_class}"]//text()').getall()).strip()
            except:
                content = None
        else:
            try:
                content = ''.join(response.xpath(f'//{content_tag}//text()').getall()).strip()
            except:
                content = None

        #  Парсим дату и время новости
        try:
            date_time = str(response.css(date_cut).get()).strip()
        except:
            date_time = None

        # Парсим дату в универсальный для обработки формат
        date = parse(date_time)

        # Получаем дату и время в формате unixtime
        nd_date = int(time.mktime(date.timetuple()))

        # Получаем дату и время в формате unixtime
        not_date = date.strftime('%d-%m-%Y')

        #  Парсим дату и время новости
        s_date = floor(time.time())

        # Сохраняем полноценные новостные структуры
        if title and content and date_time:
            yield {
                "link": link, "title": title, "content": content,
                "nd_date": nd_date, "s_date": s_date, "not_date": not_date
            }
