from selenium.webdriver.support.ui import WebDriverWait

def test_open_google(driver):
    # Открываем Google.com
    driver.get("https://www.google.com")

    # Ждем загрузки страницы (ожидаем, что URL изменится на тот, что содержит 'google.com')
    WebDriverWait(driver, 10).until(lambda d: "google.com" in d.current_url)

    # Проверка
    assert "google.com" in driver.current_url, "❌ Не удалось открыть сайт Google"