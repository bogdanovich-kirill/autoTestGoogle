from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запускаем браузер
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Находим поле для ввода
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")  # Вводим "Python"

# Проверяем, что появляются предложения в автозаполнении
try:
    suggestions = driver.find_elements(By.CSS_SELECTOR, "li.sbct")
    assert len(suggestions) > 0, "Автозаполнение не работает!"
    print(f"Найдено {len(suggestions)} предложений для поиска.")
except Exception as e:
    print(f"Ошибка: {e}")

# Закрываем браузер
time.sleep(3)
driver.quit()