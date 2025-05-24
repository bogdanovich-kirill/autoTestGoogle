from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_voice_search_button(driver):
    driver.get("https://www.google.com/?hl=ru")

    # Ждём появления кнопки голосового поиска
    voice_search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[jsname='F7uqIe']"))
    )

    assert voice_search_button.is_displayed(), "Кнопка голосового поиска не отображается на странице"