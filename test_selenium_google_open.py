from selenium import webdriver

# Создаем экземпляр веб-драйвера (например, для Chrome)
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get('https://www.google.com')

# Ждем 5 секунд, чтобы увидеть результат
import time
time.sleep(5)

# Закрываем браузер
driver.quit()