import pytest
import allure
from selenium import webdriver

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
    driver = webdriver.Chrome()  # Укажите путь к исполняемому файлу браузера, если он отличается от Chrome

    try:
        # Переходим по ссылке
        driver.get(link)

        # Далее можно добавить какие-то проверки на содержимое страницы или другие действия
        # Пример: Проверка, что заголовок страницы содержит определенный текст
        assert "escort" in driver.title, f"Failed to load link: {link}, Step: Opening page"

    except Exception as e:
        # Если произошла ошибка, добавляем ее в отчет pytest с указанием шага
        pytest.fail(f"Failed to load link: {link}, Step: Opening page. Error: {e}")

    finally:
        # В любом случае закрываем браузер после завершения теста
        driver.quit()
