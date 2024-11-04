from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.product import Product
import time
import re

def accept_cookies(driver, elements):
    accept_cookies = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, elements['accept_cookies'])))
    time.sleep(2)
    accept_cookies.click()

def get_shadow_element(driver):
    shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "impulse-search")))
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    return shadow_root

def click_show_more(shadow_root, actions, elements):
    show_more = shadow_root.find_elements(By.CSS_SELECTOR, elements['show_more_itens'])
    while len(show_more) >= 4:
        show_more_itens = show_more[3]
        actions.move_to_element(show_more_itens).perform()
        show_more_itens.click()
        time.sleep(2)
        show_more = shadow_root.find_elements(By.CSS_SELECTOR, elements['show_more_itens'])
    return show_more

def get_products(driver, elements):
    products_links = []
    products_elements = driver.find_elements(By.CSS_SELECTOR, elements['product_element'])
    for product in products_elements:
        product_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')
        products_links.append(product_link)
    return products_links

def preco_produto(driver, elements):
    preco_texto = driver.find_element(By.CSS_SELECTOR, elements).text
    preco = re.search(r'R\$\s*(\d+(?:\.\d{3})*(?:,\d{2})?)', preco_texto)  # Captura valor após R$
    if preco:
        preco = re.sub(r'[^\d,]', '', preco.group(1))  # Limpa o valor encontrado
        preco = float(preco.replace(',', '.'))  # Converte para float
        return "{:.2f}".format(preco)
    return "0.00"

def get_products_data(driver, link, elements, gender=None):
    try:
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, elements['brand_element'])))
        brand = driver.find_element(By.XPATH, elements['brand_element']).text
        product_name = driver.find_element(By.XPATH, elements['product_name']).text
        price_standard = preco_produto(driver, elements['price_standard'])
        price_sales = preco_produto(driver, elements['price_sales'])
        description = driver.find_element(By.CSS_SELECTOR, elements['description']).text
        category = driver.find_element(By.XPATH, elements['category']).text
        image_url = driver.find_element(By.XPATH, elements['img']).get_attribute('src')
        product = Product(product_name, description, price_sales, price_standard, image_url, link, category, brand, gender)
        return product
    except Exception as e:
        print(f"Erro ao obter dados do produto {link}: {e}")
        return None