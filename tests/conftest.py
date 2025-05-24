# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # без GUI
    chrome_options.add_argument("--no-sandbox")  # для CI
    chrome_options.add_argument("--disable-dev-shm-usage")  # для CI
    chrome_options.add_argument("--lang=ru-RU")
    chrome_options.add_argument("--disable-gpu")  # на всякий случай
    chrome_options.add_argument("--window-size=1920,1080")  # стабильное разрешение
    # НЕ добавлять chrome_options.add_argument("--user-data-dir=...")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()