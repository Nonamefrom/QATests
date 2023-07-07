#Запуск всех тестов через терминал из указанной папки
#  pytest ./tests
#Запуск тестов через терминал с указанием i кол-ва ранеров(число после -n {i})
#  pytest -n 3 ./tests
#
#Установка allure https://www.skill2lead.com/allure-report/allure-report-pytest-allure-report-configuration.php
#   1 Установка в терминале командой pip install allure-pytest
#   2 установка allure из скаченного файла и подключение его в PATH Windows
#   3 опросить в терминале командой allure --version должно вернуть версию, елси нет убедится в наличии JAVA
#   4 Если потребуется установить JAVA JDK 8v
#
#Конфиг запуска тестов с репортом в папку
#  --alluredir="./.reports"
#Запуск локального просмотра отчетов
#  allure serve tests/.reports
