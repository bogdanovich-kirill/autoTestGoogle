from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Ждём, пока логотип станет видимым
try:
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img.lnXdpd, svg.lnXdpd"))
    )
    print("✅ Логотип найден")
except:
    print("❌ Логотип не найден")

driver.quit()