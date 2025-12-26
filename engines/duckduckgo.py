from selenium.webdriver.common.by import By

ENGINE = {
    "name": "duckduckgo",
    "url": "https://duckduckgo.com/",
    "box": (By.NAME, "q"),
    "results": (By.CSS_SELECTOR, "div.yuRUbf a"),
}