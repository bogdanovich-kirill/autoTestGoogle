from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_autocomplete_suggestions(driver):
    driver.get("https://www.google.com")

    # Вводим запрос в поле поиска
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Python")

    # Ждём, пока появятся предложения автозаполнения
    suggestions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.sbct"))
    )

    assert len(suggestions) > 0, "Автозаполнение не работает!"