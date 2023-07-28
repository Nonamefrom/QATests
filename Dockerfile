# Используем базовый образ Python 3.10
FROM python:3.10

# Установка Allure
RUN apt-get update && apt-get install -y allure

# Установка Chrome
RUN apt-get install -y wget gnupg
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /var/www

# Копируем зависимости проекта в контейнер
COPY requirements.txt /var/www/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /var/www/

# Python будет искать модули в указанной директории /var/www.
ENV PYTHONPATH="/var/www:${PYTHONPATH}"

# Команда для запуска тестов (измените ее в соответствии с вашими настройками)
CMD ["pytest", "tests"]

WORKDIR /var/www

COPY ./requirements.txt /var/www

RUN pip install -r requirements.txt
