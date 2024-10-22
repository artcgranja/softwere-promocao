import requests
from bs4 import BeautifulSoup
import re
from utils.config import ZARA_DATA_FIELDS

def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_product_blocks(soup, fields):
    product_blocks = soup.find_all(class_=re.compile(fields['product_block']))
    return product_blocks


