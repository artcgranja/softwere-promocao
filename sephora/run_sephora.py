from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sephora.functions import accept_cookies, get_shadow_element, click_show_more, get_products, get_products_data
from utils.config import ELEMENTS_SEPHORA, SEPHORA_URL
import time

def run_sephora(driver):
    driver.get(SEPHORA_URL)
    accept_cookies(driver, ELEMENTS_SEPHORA)

    time.sleep(5)
    shadow_root = get_shadow_element(driver)
    actions = ActionChains(driver)

    campo = shadow_root.find_elements(By.CSS_SELECTOR, ELEMENTS_SEPHORA['card_element'])
    actions.move_to_element(campo[4]).perform()
    campo[4].click()

    status_view_produtos = click_show_more(shadow_root, actions, ELEMENTS_SEPHORA)
    products_links = get_products(shadow_root, ELEMENTS_SEPHORA)

    products = []
    for link in products_links:
        product = get_products_data(driver, link, ELEMENTS_SEPHORA)
        products.append(product)
    return products