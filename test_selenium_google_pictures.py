from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Проверяем, что ссылка "Картинки" присутствует
try:
    images_link = driver.find_element(By.LINK_TEXT, "Картинки")
    assert images_link.is_displayed(), "Ссылка на 'Картинки' не отображается на странице"
    print("Ссылка на 'Картинки' найдена!")
except Exception as e:
    print(f"Ошибка: {e}")

# Закрываем браузер
time.sleep(3)
driver.quit()