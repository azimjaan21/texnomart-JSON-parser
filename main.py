import time
from bs4 import BeautifulSoup
from base_parser import BaseParser
from confix import *
from mixin import ProductDeteilMixin


class CategoryParser(BaseParser, ProductDeteilMixin):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATE = {}

    def category_block_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        category_links = soup.find_all('a', class_='category__link')
        for category in category_links:
            category_title = category.find('h2', class_='content__title').get_text(strip=True)
            print(style.BLUE + category_title)
            self.DATE[category_title] = []
            category_link = self.host + category.get('href')
            print(category_link)

            category_page = self.get_html(category_link)
            self.category_page_parser(category_page, category_title)

    def category_page_parser(self, category_page, category_title):
        soup = BeautifulSoup(category_page, 'html.parser')
        section = soup.find('div', class_='products-box')
        products = section.find_all('div', class_='product-item-wrapper')
        for product in products[:3]:
            product_name = product.find('a', class_='product-name').get_text(strip=True)
            print(style.RED + product_name)
            product_price = product.find('div', class_='d-flex align-center justify-between w-full').get_text(
                strip=True)
            print(style.YELLOW + product_price)
            product_link = self.host + product.find('a', class_='product-link').get('href')
            print(product_link)

            product_detail_page = self.get_html(product_link)
            characteristics = self.get_deteil_info(product_detail_page)

            self.DATE[category_title].append({
                'product_name': product_name,
                'product_price': product_price,
                'product_link': product_link,
                'characteristics': characteristics
            })


def start_category_parsing():
    parser = CategoryParser()

    category = input('Введите категорию: ')
    category_link = 'https://texnomart.uz/ru/katalog/' + category
    print('Парсер начал работу')
    start = time.time()
    html = parser.get_html(category_link)
    parser.category_block_parser(html)

    parser.save_date_to_json(category, parser.DATE)
    finish = time.time()

    print(f'Парсер завершил работу за {round(finish - start, 2)} секунд')


start_category_parsing()
