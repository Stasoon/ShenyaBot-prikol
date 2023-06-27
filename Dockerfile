# установка базового образа (host OS)
FROM FROM python:3.8-slim

# Установка рабочей директории в контейнере
WORKDIR /bot

# Копирование всех файлов в рабочую директорию контейнера
COPY . .

# Установка зависимостей
RUN pip install venv
RUN source venv/Scripts/activate
RUN pip install -r requirements.txt

# команда, выполняемая при запуске контейнера
CMD [ "python", "main.py" ]