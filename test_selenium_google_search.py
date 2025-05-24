from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Это нужно для симуляции нажатия клавиш

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Открываем страницу Google
driver.get("https://www.google.com")

# Находим элемент поисковой строки
search_box = driver.find_element("name", "q")  # Это имя элемента на странице

# Вводим запрос и нажимаем Enter
search_box.send_keys("Selenium Python")  # Вводим запрос
search_box.send_keys(Keys.RETURN)  # Нажимаем Enter

# Ждем несколько секунд, чтобы увидеть результат
import time
time.sleep(5)

# Закрываем браузер
driver.quit()