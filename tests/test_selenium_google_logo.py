# test_selenium_google_logo.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_logo_visible(driver):
    driver.get("https://www.google.com/?hl=ru")

    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img.lnXdpd, svg.lnXdpd"))
    )

    assert logo.is_displayed(), "❌ Логотип Google не отображается"