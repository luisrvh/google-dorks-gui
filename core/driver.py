import os
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


def base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_driver():
    driver_path = os.path.join(base_dir(), "msedgedriver.exe")

    if not os.path.exists(driver_path):
        raise FileNotFoundError("msedgedriver.exe no encontrado")

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    return webdriver.Edge(
        service=Service(driver_path),
        options=options
    )
