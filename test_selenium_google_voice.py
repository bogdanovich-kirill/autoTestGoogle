from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Проверяем наличие кнопки голосового поиска
try:
    voice_search_button = driver.find_element(By.CSS_SELECTOR, "div[jsname='F7uqIe']")
    assert voice_search_button.is_displayed(), "Кнопка голосового поиска не отображается на странице"
    print("Кнопка голосового поиска найдена!")
except Exception as e:
    print(f"Ошибка: {e}")

# Закрываем браузер
time.sleep(3)
driver.quit()