# установка базового образа (host OS)
FROM python:3.8-slim

# Установка рабочей директории в контейнере
WORKDIR /bot

# Копирование всех файлов в рабочую директорию контейнера
COPY . .

# Установка зависимостей
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080/tcp

# команда, выполняемая при запуске контейнера
CMD [ "python", "main.py" ]