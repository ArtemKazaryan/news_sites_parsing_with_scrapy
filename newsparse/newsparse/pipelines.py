# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class NewsparsePipeline:
#     def process_item(self, item, spider):
#         return item



#
import sqlite3
class NewsparsePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('parsenews.db')
        self.cursor = self.conn.cursor()
        # Создание таблицы "items", если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT,
                title TEXT,
                content TEXT,
                nd_date TEXT,
                s_date TEXT,
                not_date TEXT
            )
        ''')
        self.conn.commit()
    def close_spider(self, spider):
        self.conn.close()
    def process_item(self, item, spider):
        # Вставка данных в таблицу "items"
        self.cursor.execute('''
            INSERT INTO items (link, title, content, nd_date, s_date, not_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item.get('link'),
            item.get('title'),
            item.get('content'),
            item.get('nd_date'),
            item.get('s_date'),
            item.get('not_date')
        ))
        self.conn.commit()
        return item