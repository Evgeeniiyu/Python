# Базовий образ Python
FROM python:3.10-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлів у контейнер
COPY . /app

# Встановлення Flask
RUN pip install --no-cache-dir Flask

# Вказуємо порт для Flask
EXPOSE 5000

# Команда для запуску додатку
CMD ["python", "app.py"]
