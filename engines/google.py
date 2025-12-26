from selenium.webdriver.common.by import By

ENGINE = {
    "name": "Google",
    "url": "https://www.google.com",
    "box": (By.NAME, "q"),
    "results": (By.CSS_SELECTOR, "div.yuRUbf a"),
}
