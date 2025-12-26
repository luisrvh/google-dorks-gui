import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.driver import get_driver


def run_search(engine, dork, wait=20):
    driver = get_driver()
    results = []

    try:
        driver.get(engine["url"])

        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located(engine["box"])
        )

        box = driver.find_element(*engine["box"])
        box.send_keys(dork)
        box.send_keys(Keys.RETURN)

        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located(engine["results"])
        )

        links = driver.find_elements(*engine["results"])

        for l in links[:10]:
            results.append((l.text.strip(), l.get_attribute("href")))

        time.sleep(random.uniform(2, 4))

    finally:
        driver.quit()

    return results
