import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search_button_click(driver):
    driver.get("https://www.google.com")

    # Вводим запрос в строку поиска
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    time.sleep(1)  # Короткая задержка, чтобы кнопка btnK стала видимой

    # Ждём, пока кнопка поиска станет кликабельной, и нажимаем
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnK"))
    )
    search_button.click()

    # Ждём, пока появятся результаты поиска
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Проверяем, что результат поиска содержит текст
    assert "Selenium" in driver.page_source, "❌ Результаты поиска не отобразились"