import requests
from parsel import Selector
from pprint import pprint
import sqlite3

MAIN_URL = 'https://cars.kg/offers'
URL = 'https://cars.kg'
def get_html(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception('error')

def parse_html(html: str):
    selector = Selector(text=html)
    return selector

def get_title(selector: Selector):
    return selector.css('title::text').get()

def get_cars(selector: Selector):
    return selector.css('').get()

def clean_text(text: str):
    if text is None:
        return ''

    text = text.strip()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    return text

def cars_info(selector: Selector):
    car_info = []
    for car in selector.css('.catalog-list .catalog-list-item'):
        cars_info = {}
        cars_info['title'] = clean_text(car.css('span.catalog-item-caption::text\n').get())
        cars_info['year'] = clean_text(car.css('span.caption-year::text\n').get())
        cars_info['price'] = clean_text(car.css('span.catalog-item-price::text\n').get())
        cars_info['url'] = f'{URL}{car.css("a").attrib.get("href")}'
        car_info.append(cars_info)

    return car_info

def main():
    html = get_html(f"{MAIN_URL}")
    # pprint(html[:300])
    selector = parse_html(html)
    pprint(cars_info(selector))
