from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def iniciar_selenium():
    opcoes = Options()
    opcoes.add_argument('--start-maximized')
    
    opcoes.add_experimental_option("prefs", {
        "profile.default_content_settings.css": 2
    })
    
    driver_path = EdgeChromiumDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=opcoes)
    
    return driver

def clicar_elemento(driver, xpath):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elemento)
        elemento.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento: {e}")
        return False
    
def aguardar_elemento(driver, xpath, tempo_espera=15):
    try:
        WebDriverWait(driver, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return True
    except:
        return False

def get_element_xpath(driver, element):
    return driver.execute_script("""
    function getElementXPath(element) {
        if (element.id !== '') {
            return 'id("' + element.id + '")';
        }
        if (element === document.body) {
            return element.tagName.toLowerCase();
        }

        var ix = 0;
        var siblings = element.parentNode.childNodes;
        for (var i = 0; i < siblings.length; i++) {
            var sibling = siblings[i];
            if (sibling === element) {
                return getElementXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix + 1) + ']';
            }
            if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                ix++;
            }
        }
    }
    return getElementXPath(arguments[0]);
    """, element)