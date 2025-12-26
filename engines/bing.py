from selenium.webdriver.common.by import By

ENGINE = {
    "name": "bing",
    "url": "https://www.bing.com/",
    "box": (By.NAME, "q"),
    "results": (By.CSS_SELECTOR, "div.yuRUbf a"),
}


