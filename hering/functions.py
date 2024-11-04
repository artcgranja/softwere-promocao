from driver.selenium_functions import aguardar_elemento
from models.product import Product
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def descricao_produto(driver):
    aguardar_elemento(driver, '//*[@id="product-main"]/div[1]/div[1]/section[10]/div/div')
    descricao_compelta = driver.find_element(By.XPATH, '//*[@id="product-main"]/div[1]/div[1]/section[10]/div/div').text
    descricoes = descricao_compelta.split('\n')
    descricao = descricoes[2]
    return descricao.replace("'", '')

def preco_produto(driver):
    aguardar_elemento(driver, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[4]/div/span[2]')
    preco_texto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[4]/div/span[2]').text
    preco = preco_texto.split('R$')
    preco = preco[1].split(' ')
    return preco[1].replace(',', '.')

def preco_antigo_produto(driver):
    aguardar_elemento(driver, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[4]/div/span[1]')
    preco_antigo_texto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[4]/div/span[1]').text
    preco_antigo = preco_antigo_texto.split('R$')[1].split(' ')
    return preco_antigo[1].replace(',', '.')

def name_produto(driver):
    aguardar_elemento(driver, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[2]/h1")
    name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[2]/h1").text
    return name.replace("'", '')

def get_links(driver):
    links = []
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hering-hering-components-3-x-galleryItemWrapper")))
    for element in elements:
        aguardar_elemento(driver, ".hering-hering-components-3-x-galleryCustomShelf")
        element_link = element.find_element(By.CSS_SELECTOR, ".hering-hering-components-3-x-galleryCustomShelf")
        link_product = element_link.get_attribute("href")
        links.append(link_product)
    return links

def get_products(driver, link, category, gender=None):
    try:
        driver.get(link)
        aguardar_elemento(driver, '//*[@id="product-main"]/div[1]/div[1]/section[10]/div/div/text()[2]')
        name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/main/div[1]/div[1]/section[2]/h1").text
        descricao = descricao_produto(driver)
        price = preco_produto(driver)
        price_old = preco_antigo_produto(driver)
        link_img = driver.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        produto = Product(name, descricao, price, price_old, link_img, link, category, 'Hering', gender)
    except:
        return None
    return produto