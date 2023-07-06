import allure
from pages.base_page import BasePage
from pages.keycloack_auth_page import keycloack_auth_form

CPurl = 'https://develop-cp.dev.svrauto.ru/auth/login'
email = 'admin@svrauto.ru'
wrongemail = 'admin@admin@ru23'
wronguserpass = '123456789'
userpass = 'adminPass'
errortext = 'Неправильное имя пользователя или пароль.'

@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов Панели Управления")
#Авторизация существующего пользователя ПУ с неправильным паролем
@allure.title("Авторизация сущест. пользователя с неправильным паролем")
def test_login_wrongPass(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = keycloack_auth_form(driver, url=CPurl)
    auth_form.login(email, wronguserpass)
    assert errortext == auth_form.error_message(), "Wrong error text"

#Авторизация НЕсуществующего пользователя ПУ с правильным паролем
@allure.title("Авторизация НЕсущест. пользователя с правильным паролем")
def test_login_wrongMail(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = keycloack_auth_form(driver, url=CPurl)
    auth_form.login(wrongemail, userpass)
    assert errortext == auth_form.error_message(), "Wrong error text"

#Авторизация существующего пользователя ПУ с правильным паролем
@allure.title("Авторизация корректного пользователя")
def test_login_correctUser(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = keycloack_auth_form(driver, url=CPurl)
    auth_form.login(email, userpass)
    assert 'Панель управления' == driver.title, "Wrong title of page, or wrong page was loaded"