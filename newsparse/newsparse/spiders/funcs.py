import sqlite3
from typing import List, Any

from selenium import webdriver
from bs4 import BeautifulSoup
import time

import time
from playwright.sync_api import sync_playwright


def end_load(level_depth, load_pause, menu_url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(menu_url)
        for i in range(level_depth + 1):
            page.keyboard.press('End')
            time.sleep(load_pause)
        html = page.content()
    return html


def scroll_load(level_depth, load_pause, menu_url):
    driver = webdriver.Chrome()
    driver.get(menu_url)
    for i in range(level_depth + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(load_pause)

    html = driver.page_source
    return html


def create_tables_and_add_resources(db_name, resources):
    conn = sqlite3.connect(db_name)

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS resource(
        resource_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        resource_name TEXT,
        resource_url TEXT,
        top_tag TEXT,
        bottom_tag TEXT,
        title_cut TEXT,
        date_cut TEXT);
    """)
    conn.commit()

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        res_id INT,
        link TEXT,
        title TEXT,
        content TEXT,
        nd_date TEXT,
        s_date TEXT,
        not_date TEXT);
    """)
    conn.commit()

    cur.executemany("INSERT INTO resource(resource_name, resource_url, top_tag, bottom_tag, title_cut, date_cut)"
                    " VALUES(?, ?, ?, ?, ?, ?);", resources)
    conn.commit()
    conn.close()


def add_to_items(db_name, resource_id, link, title, content, nd_date, s_date, not_date):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    news_item_obj = (resource_id, link, title, content, nd_date, s_date, not_date)
    cur.execute("""INSERT INTO items(res_id, link, title, content, nd_date, s_date, not_date) VALUES(?, ?, ?, ?, ?, ?, ?);""",
                news_item_obj)
    conn.commit()
    conn.close()
