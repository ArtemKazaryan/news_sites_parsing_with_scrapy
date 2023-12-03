resources = [
        ('Новостной портал nur.kz', 'https://nur.kz/latest, scrolling 4 2',
         'block-infinite js-infinite, div, article-preview-category__content, a',
         'formatted-body__content--wrapper, div',
         'main-headline js-main-headline, h1', '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)'),
        ('Новостной портал scientificrussia.ru',
         'https://scientificrussia.ru/news, pagination 1134 1130 -1 f"https://scientificrussia.ru/news/{i}"',
         'image, div, , a',
         'article-text, div', ', h1', '%Y-%m-%d %H:%M, time::attr(datetime)'),
        ('Новостной портал tengrinews.kz',
         'https://tengrinews.kz/news, pagination 1 5 1 f"https://tengrinews.kz/news/page/{i}"',
         'tn-article-grid, div, tn-link, a',
         'tn-news-content, div', 'tn-content-title, h1', '(СегодняOrВчераOr%d%b%Y)comma%H:%M, time::text'),
        ('Горнопромышленный портал mining.kz',
         'https://mining.kz/ru/novosti-kazakhstana, pagination 1 5 1 f"https://mining.kz/ru/novosti-kazakhstana?start={i-1}0"',
         'itemList, div, , a',
         'itemFullText, div', 'itemTitle, h1', '(ДеньНедели)comma%d%b%Y, span.itemDateCreated::text')
]




# Резервные переменные

# nur.kz
# resource_name = 'Новостной портал nur.kz'
# resource_url = 'https://nur.kz/latest, scrolling 4 2'
# top_tag = 'block-infinite js-infinite, div, article-preview-category__content, a'
# bottom_tag = 'formatted-body__content--wrapper, div'
# title_cut = 'main-headline js-main-headline, h1'
# date_cut = '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)'

# scientificrussia.ru
# resource_name = 'Новостной портал scientificrussia.ru'
# resource_url = 'https://scientificrussia.ru/news, pagination 1134 1130 -1 f"https://scientificrussia.ru/news/{i}"'
# top_tag = 'image, div, , a'
# bottom_tag = 'article-text, div'
# title_cut = ', h1'
# date_cut = '%Y-%m-%d %H:%M, time::attr(datetime)'

# tengrinews.kz
# resource_name = 'Новостной портал tengrinews.kz'
# resource_url = 'https://tengrinews.kz/news, pagination 1 5 1 f"https://tengrinews.kz/news/page/{i}"'
# top_tag = 'tn-article-grid, div, tn-link, a'
# bottom_tag = 'tn-news-content, div'
# title_cut = 'tn-content-title, h1'
# date_cut = '(СегодняOrВчераOr%d%b%Y)comma%H:%M, time::text'


# from dateparser import parse
# date_string = 'Вчера, 13:26'
# try:
#     date = parse(date_string)
#     print(date)
# except:
#     print('Дата не может быть разобрана')

# import time
# from dateutil.relativedelta import relativedelta
# from dateparser.parse import parse

# import time
# from dateparser import parse
# date_string='Вчера, 13:31'
# date = parse(date_string)
# print(int(time.mktime(date.timetuple())))
# print(date.strftime('%d-%m-%Y'))


# import yaml
# with open("nurkz.yaml") as file:
#     loaded_yaml = yaml.load(file, Loader=yaml.FullLoader)
#     print(loaded_yaml['extract_samples']['fields'])
#     print(loaded_yaml)
#     print(loaded_yaml['configuration']['settings']['crawl_strategy']['type'])
# # for key, value in loaded_yaml.items():
# #     print(f"{key}: {value}")
# # print()



# from urllib.request import urlopen
#
# url = 'http://mining.kz/robots.txt'
# content = urlopen(url).read().decode('utf-8')
# print(content)

# from requests_toolbelt import disable_verify
# import requests
# url = "http://www.mining.kz"
# response = requests.get(url, verify=False)
# print(response.text)

# from requests_toolbelt import disable_verify
# import requests
#
# url = "http://www.mining.kz"
# response = requests.get(url, verify=False)
# print(response.text)



# Начало файла
# # Импортируем модуль scrapy
# import scrapy
# import time
# import sqlite3
#
# # Импортируем функцию add_to_items из funcs.py
# from .funcs import add_to_items
#
# # Импортируем список кортежей управляющих структур
# from .resources import resources
#
# # Задаём базы данных
# db_name = 'parsenews.db'
#
# # Строки с 12 по 17 НЕ РАСКОММЕНТИРОВЫВАТЬ!!!
# # Импортируем список кортежей для работы с sqlite3 из  resources.py
# # Импортируем функцию create_tables_and_add_resources из funcs.py
# # from .funcs import create_tables_and_add_resources
# # create_tables_and_add_resources(db_name, resources)
#
#
# # Выводим меню для выбора новостного сайта
# site_choice = input(f'Выбери новостной сайт для парсинга: '
#                     f'1-nur.kz; '
#                     f'2-scientificrussia.ru; '
#                     f'3-tengrinews.kz; '
#                     f'4-mining.kz; '
#                     f'0-Выход;'
#                     f'__: ')
# if site_choice == '0':
#     quit()
# elif site_choice == '1':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал nur.kz';"
# elif site_choice == '2':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал scientificrussia.ru';"
# elif site_choice == '3':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал tengrinews.kz';"
# elif site_choice == '4':
#     select = f"SELECT * FROM resource WHERE resource_name='Горнопромышленный портал mining.kz';"
#
# # Связываемся с БД и производим выполнение выбранной команды
# conn = sqlite3.connect(db_name)
# cur = conn.cursor()
# cur.execute(select)
# # Получаем данные из БД
# result = cur.fetchone()
# res = list(result)
#
# # Производим передачу и распаковку данных из таблицы resource
# # ДЛЯ НАГЛЯДНОСТИ переопределяем переменные
# resource_id = res[0]
# resource_url_args = res[2].split(', ')
# depth_config = resource_url_args[1].split(', ')
# depth_mode = depth_config[0].split(' ')
# top_tag_args = res[3].split(', ')
# bottom_tag_args = res[4].split(', ')
# title_cut_args = res[5].split(', ')
# date_cut_args = res[6].split(', ')
#
#
# # Создаём класс паука и его методов
# class NewsSpider(scrapy.Spider):
#     name = 'news_spider'
#
#     # start_urls = {
#     #     'https://nur.kz/latest',
#     #     'https://scientificrussia.ru/news',
#     #     'https://tengrinews.kz/news',
#     #     'https://mining.kz/ru/novosti-kazakhstana'
#     # }
#
#     start_urls = {
#         resource_url_args[0]
#     }
#     # def __init__(self, *args, **kwargs):
#     #     ...
#
#     # Метод парсинга, в котором производится получение URL-адресов новостей
#     def parse(self, response):
#         # При наличии параметра scrolling сайта
#         if depth_mode[0] == 'scrolling':
#             # Импортируем функции для дозагрузки данных на странице: scroll_load (Selenium) и end_load (Playwright)
#             from .funcs import scroll_load, end_load
#             from bs4 import BeautifulSoup
#             # Формируем удобочитаемые переменные для передачи их в функцию scroll_load или в функцию end_load
#             level_depth, load_pause = int(depth_mode[1]) - 1, float(depth_mode[2])
#             menu_url, div1_tag_class, div1_tag, a_tag_class, a_tag =\
#                 resource_url_args[0], top_tag_args[0], top_tag_args[1], top_tag_args[2], top_tag_args[3]
#
#             # Получаем URL-адреса новостей
#             # html = scroll_load(level_depth, load_pause, menu_url) # на selenium
#             html = end_load(level_depth, load_pause, menu_url)      # на playwright
#             soup = BeautifulSoup(html, "html.parser")
#             links0 = soup.find_all(div1_tag, class_=div1_tag_class)
#             links = []
#             for link0 in links0:
#                 links1 = link0.find_all(a_tag, class_=a_tag_class)
#                 for link1 in links1:
#                     links.insert(0, link1["href"])
#
#             # Передаём их URL-адреса в функцию парсинга parse_news
#             for link in links:
#                 yield response.follow(link, callback=self.parse_news)
#
#         # При наличии параметра pagination сайта
#         elif depth_mode[0] == 'pagination':
#             # Получение удобочитаемых переменных
#             start, end, step, page_link = depth_mode[1], depth_mode[2], depth_mode[3], depth_mode[4]
#             div1_tag_class, div1_tag, a_tag_class, a_tag = top_tag_args[0], top_tag_args[1], top_tag_args[2], top_tag_args[3]
#
#             # Проверка на наличие пустых полей для корректной работы механизма xpath
#             if div1_tag_class != '':
#                 div1_tag_class = f'[@class="{div1_tag_class}"]'
#             if a_tag_class != '':
#                 a_tag_class = f'[@class="{a_tag_class}"]'
#
#             # Получаем URL-адреса новостей и передаём их URL-адреса в функцию парсинга parse_news
#             for link in response.xpath(f'//{div1_tag}{div1_tag_class}//{a_tag}{a_tag_class}/@href').extract():
#                 yield response.follow(link, callback=self.parse_news)
#
#             # Проверка последовательности пагинации
#             # Справа налево
#             if int(start) > int(end):
#                 for i in range(int(start), int(end)-1, int(step)):
#                     next_page = eval(page_link)
#                     yield response.follow(next_page, callback=self.parse)
#             # Слева направо
#             elif int(start) < int(end):
#                 for i in range(int(start)+1, int(end)+1, int(step)):
#                     next_page = eval(page_link)
#                     yield response.follow(next_page, callback=self.parse)
#
#
#     def parse_news(self, response):
#         # Импортируем модуль для округления в меньшую сторону
#         from math import floor
#         # Импортируем модуль получения даты
#         from dateparser import parse
#
#         # Получаем ссылку как атрибут объекта response, переданную  в генераторе функции parse
#         link = response.url
#
#         # Получение удобочитаемых переменных
#         h1_tag_class, h1_tag = title_cut_args[0], title_cut_args[1]
#         # Проверка на пустые поля для корректной работы механизма xpath
#         if h1_tag_class != '':
#             h1_tag_class = f'[@class="{h1_tag_class}"]'
#         title = str(response.xpath(f'//{h1_tag}{h1_tag_class}/text()').get()).strip()
#
#         # Получение удобочитаемых переменных
#         div2_tag_class, div2_tag = bottom_tag_args[0], bottom_tag_args[1]
#         # Проверка на пустые поля для корректной работы механизма xpath
#         if div2_tag_class != '':
#             div2_tag_class = f'[@class="{div2_tag_class}"]'
#         content = ''.join(response.xpath(f'//{div2_tag}{div2_tag_class}//text()').getall()).strip()
#
#         # Получение переменной css-селектора для получения даты и времени новости
#         css_date_arg = date_cut_args[1]
#         date_time = str(response.css(css_date_arg).get()).strip()
#         date = parse(date_time)
#         nd_date = int(time.mktime(date.timetuple()))
#         not_date = date.strftime('%d-%m-%Y')
#
#         # Получение времени внесения данных в БД
#         s_date = floor(time.time())
#
#         # # Вызов функции add_to_items добавления данных новости в ручную в таблицу items БД parsenews.db (необходимо раскомментировать),
#         # # иначе сохранение в БД настроено с помощью активации конвеера pipelines.py в settings.py сохраняется в news.db
#         # add_to_items(db_name, resource_id, link, title, content, nd_date, s_date, not_date)
#
#         # Для формирования словаря, который можно сохранять в json-файл, например
#         yield {
#             "res_id": resource_id, "link": link, "title": title, "content": content,
#             "nd_date": nd_date, "s_date": s_date, "not_date": not_date
#         }
#


# Импортируем модуль scrapy
import scrapy
import time
import sqlite3
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import yaml

# Импортируем функцию add_to_items из funcs.py
# from .funcs import add_to_items

# Импортируем список кортежей управляющих структур
# from .resources import resources

# Задаём базы данных
db_name = 'parsenews.db'

# Строки с 12 по 17 НЕ РАСКОММЕНТИРОВЫВАТЬ!!!
# Импортируем список кортежей для работы с sqlite3 из  resources.py
# Импортируем функцию create_tables_and_add_resources из funcs.py
# from .funcs import create_tables_and_add_resources
# create_tables_and_add_resources(db_name, resources)


# # Выводим меню для выбора новостного сайта
# site_choice = input(f'Выбери новостной сайт для парсинга: '
#                     f'1-nur.kz; '
#                     f'2-scientificrussia.ru; '
#                     f'3-tengrinews.kz; '
#                     f'4-mining.kz; '
#                     f'0-Выход;'
#                     f'__: ')
# if site_choice == '0':
#     quit()
# elif site_choice == '1':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал nur.kz';"
# elif site_choice == '2':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал scientificrussia.ru';"
# elif site_choice == '3':
#     select = f"SELECT * FROM resource WHERE resource_name='Новостной портал tengrinews.kz';"
# elif site_choice == '4':
#     select = f"SELECT * FROM resource WHERE resource_name='Горнопромышленный портал mining.kz';"
#
# # Связываемся с БД и производим выполнение выбранной команды
# conn = sqlite3.connect(db_name)
# cur = conn.cursor()
# cur.execute(select)
# # Получаем данные из БД
# result = cur.fetchone()
# res = list(result)
#
# # Производим передачу и распаковку данных из таблицы resource
# # ДЛЯ НАГЛЯДНОСТИ переопределяем переменные
# resource_id = res[0]
# resource_url_args = res[2].split(', ')
# depth_config = resource_url_args[1].split(', ')
# depth_mode = depth_config[0].split(' ')
# top_tag_args = res[3].split(', ')
# bottom_tag_args = res[4].split(', ')
# title_cut_args = res[5].split(', ')
# date_cut_args = res[6].split(', ')