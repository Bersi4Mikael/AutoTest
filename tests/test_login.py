import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Определение времени ожидания
wait_time = 10

def get_links():
    # Читаем ссылки из файла
    with open('links.txt', 'r') as file:
        links = file.readlines()
    # Удаляем пробельные символы в начале и в конце строки и возвращаем список ссылок
    return [link.strip() for link in links]

@pytest.mark.parametrize("link", get_links())
@allure.feature("Моя фича")
@allure.story("Мой сценарий")
@allure.title("Тест на заголовок страницы")
def test_links(link):
    # Запускаем веб-браузер перед каждым тестом
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()  # Укажите путь к исполняемому файлу браузера, если он отличается от Chrome
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 1024)

    try:
        # Переходим по ссылке
        driver.get(link)

        # Используем WebDriverWait для ожидания загрузки страницы
        WebDriverWait(driver, wait_time).until(EC.title_contains("escort"))
        
        # Закрытие приветственного окна
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='render-box']/button"))
        )
        element.click()

        # Переход на Стр. авторизации
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='hamburger']"))
        )
        element.click()
        
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/header/div[4]/nav/ul/li[22]"))
        )
        element.click(), f"Failed to load link: {link}, Step: Login page"

        # Ввод данных и вход        
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='form-user']"))
        )
        element.send_keys("Cawinom212")
        
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='form-pass']"))
        )
        element.send_keys("Cawinom212")

        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='submit-login']"))
        )
        element.click()

        # Далее можно добавить какие-то проверки на содержимое страницы или другие действия
        # Пример: Проверка, что заголовок страницы содержит определенный текст
        assert "escort" in driver.title, f"Failed to load link: {link}, Step: Opening page"

    except Exception as e:
        # Если произошла ошибка, добавляем ее в отчет pytest с указанием шага
        pytest.fail(f"Failed to load link: {link}, Step: Opening page. Error: {e}")

    finally:
        # В любом случае закрываем браузер после завершения теста
        driver.quit()
