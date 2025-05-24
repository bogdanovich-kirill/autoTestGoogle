from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_images_link_visible(driver):
    driver.get("https://www.google.com/?hl=ru")

    # Ждём появления ссылки "Картинки"
    images_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Картинки"))
    )

    # Проверка
    assert images_link.is_displayed(), "❌ Ссылка 'Картинки' не отображается на странице"