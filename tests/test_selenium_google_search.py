from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search(driver):
    driver.get("https://www.google.com")

    # Ожидаем появление поисковой строки и вводим запрос
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Ждём, пока результаты загрузятся
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Проверяем, что на странице есть текст "Selenium Python"
    assert "Selenium" in driver.page_source or "Python" in driver.page_source, "❌ Результаты поиска не найдены"