# Импортируем модуль scrapy
import scrapy
import time
import sqlite3
# Импортируем функцию add_to_items из funcs.py
from .funcs import add_to_items

# Задаём базы данных
db_name = 'parsenews.db'

# Строки 12, 13, 14, 15 и 16 НЕ РАСКОММЕНТИРОВЫВАТЬ!!!
# Импортируем список кортежей для работы с sqlite3 из  resources.py
# from .resources import resources
# # Импортируем функцию create_tables_and_add_resources из funcs.py
# from .funcs import create_tables_and_add_resources
# create_tables_and_add_resources(db_name, resources)


selects = []
# Выводим меню для выбора новостного сайта
site_choice = input(f'Выбери новостной сайт для парсинга: '
                    f'1-nur.kz; '
                    f'2-scientificrussia.ru; '
                    f'3-tengrinews.kz; '
                    f'0-Выход;'
                    f'__: ')
if site_choice == '0':
    quit()
elif site_choice == '1':
    select = "SELECT * FROM resource WHERE resource_name='Новостной портал nur.kz';"
elif site_choice == '2':
    select = "SELECT * FROM resource WHERE resource_name='Новостной портал scientificrussia.ru';"
elif site_choice == '3':
    select = "SELECT * FROM resource WHERE resource_name='Новостной портал tengrinews.kz';"

start_time = time.time()

# Связываемся с БД и производим выполнение выбранной команды
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute(select)
result = cur.fetchone()
res = list(result)

# Производим передачу и распаковку данных из таблицы resource
# ДЛЯ НАГЛЯДНОСТИ переопределяем переменные
resource_id = res[0]
resource_url_args = res[2].split(', ')
depth_config = resource_url_args[1].split(', ')
depth_mode = depth_config[0].split(' ')

top_tag_args = res[3].split(', ')
bottom_tag_args = res[4].split(', ')
title_cut_args = res[5].split(', ')
date_cut_args = res[6].split(', ')

# Создаём класс паука и его методов
class NewsSpider(scrapy.Spider):
    name = 'news_spider'
    start_urls = {
        resource_url_args[0]
    }

    # Метод парсинга, в котором производится получение URL-адресов новостей
    def parse(self, response):
        # При наличии параметра scrolling сайта
        if depth_mode[0] == 'scrolling':
            from .funcs import scroll_load
            # Формируем удобочитаемые переменные для передачи их в функцию scroll_load
            level_depth, load_pause = int(depth_mode[1]) - 1, int(depth_mode[2])
            menu_url, div1_tag_class, div1_tag, a_tag_class, a_tag =\
                resource_url_args[0], top_tag_args[0], top_tag_args[1], top_tag_args[2], top_tag_args[3]

            # Получаем URL-адреса новостей
            links = scroll_load(level_depth, load_pause, menu_url, div1_tag_class, div1_tag, a_tag_class, a_tag)
            # Передаём их URL-адреса в функцию парсинга parse_news
            for link in links:
                yield response.follow(link, callback=self.parse_news)

        # При наличии параметра pagination сайта
        elif depth_mode[0] == 'pagination':
            # Получение удобочитаемых переменных
            start, end, step, page_link = depth_mode[1], depth_mode[2], depth_mode[3], depth_mode[4]
            div1_tag_class, div1_tag, a_tag_class, a_tag = top_tag_args[0], top_tag_args[1], top_tag_args[2], top_tag_args[3]

            # Проверка на пустые поля для корректной работы механизма xpath
            if div1_tag_class != '':
                div1_tag_class = f'[@class="{div1_tag_class}"]'
            if a_tag_class != '':
                a_tag_class = f'[@class="{a_tag_class}"]'

            # Получаем URL-адреса новостей и передаём их URL-адреса в функцию парсинга parse_news
            for link in response.xpath(f'//{div1_tag}{div1_tag_class}//{a_tag}{a_tag_class}/@href').extract():
                yield response.follow(link, callback=self.parse_news)

            # Проверка последовательности пагнации
            # Справа налево
            if int(start) > int(end):
                for i in range(int(start), int(end)-1, int(step)):
                    next_page = eval(page_link)
                    yield response.follow(next_page, callback=self.parse)
            # Слева направо
            elif int(start) < int(end):
                for i in range(int(start)+1, int(end)+1, int(step)):
                    next_page = eval(page_link)
                    yield response.follow(next_page, callback=self.parse)

    def parse_news(self, response):
        # Импортируем модуль для округления в меньшую сторону
        from math import floor
        # Импортируем модуль получения даты
        import datetime

        # Получаем ссылку как атрибут объекта response, переданную  в генераторе функции parse
        link = response.url

        # Получение удобочитаемых переменных
        h1_tag_class, h1_tag = title_cut_args[0], title_cut_args[1]
        # Проверка на пустые поля для корректной работы механизма xpath
        if h1_tag_class != '':
            h1_tag_class = f'[@class="{h1_tag_class}"]'
        title = str(response.xpath(f'//{h1_tag}{h1_tag_class}/text()').get()).strip()

        # Получение удобочитаемых переменных
        div2_tag_class, div2_tag = bottom_tag_args[0], bottom_tag_args[1]
        # Проверка на пустые поля для корректной работы механизма xpath
        if div2_tag_class != '':
            div2_tag_class = f'[@class="{div2_tag_class}"]'
        content = ''.join(response.xpath(f'//{div2_tag}{div2_tag_class}//text()').getall()).strip()

        # Получение переменной css-селектора для получения даты и времени новости
        css_date_arg = date_cut_args[1]
        date_time = str(response.css(css_date_arg).get()).strip()
        # import time
        from dateparser import parse
        date = parse(date_time)
        nd_date = int(time.mktime(date.timetuple()))
        not_date = date.strftime('%d-%m-%Y')

        # Получение времени внесения данных в БД
        s_date = floor(time.time())
        # Вызов функции добавления данных новости в таблицу items БД
        add_to_items(db_name, resource_id, link, title, content, nd_date, s_date, not_date)
        # Остановка парсинг-таймера
        end_time = time.time()
        print(f'ДЛИТЕЛЬНОСТЬ ПАРСИНГА: {round(end_time - start_time, 2)} СЕКУНД')
        # Для формирования словаря, который можно сохранять в json-файл
        yield {
            "res_id": resource_id, "link": link, "title": title, "content": content,
            "nd_date": nd_date, "s_date": s_date, "not_date": not_date
        }

