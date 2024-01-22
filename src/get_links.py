from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_links(min_amount):
    """
    Obtiene enlaces de noticias de la página de New York Times relacionadas con la empresa Alphabet Inc.

    Parámetros:
        min_amount (int): La cantidad mínima de enlaces que se desean obtener.

    Devoluciones:
        list: Una lista de enlaces de noticias.

    Uso:
        links = get_links(10)
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nytimes.com/topic/company/alphabet-inc")

    time.sleep(5)

    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")

    links = []

    while len(links) < min_amount:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

        news_elements = driver.find_elements(by=By.CLASS_NAME, value="css-8hzhxf")
        for elem in news_elements:
            if elem.get_attribute('href') not in links and elem:
                links.append(elem.get_attribute('href'))

    driver.quit()
    return links
