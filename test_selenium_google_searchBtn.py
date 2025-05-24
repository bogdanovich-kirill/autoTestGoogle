from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запускаем браузер
driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Находим поле ввода
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("Selenium Python")

# Ждем, пока кнопка станет кликабельной
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)
search_button.click()

# Ждем, чтобы увидеть результаты
time.sleep(5)

assert driver.find_element(By.NAME, "btnK").is_displayed(), "Кнопка не найдена"

# Закрываем браузер
driver.quit()