# Используем более полный базовый образ
FROM ubuntu:22.04

# Устанавливаем зависимости
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем переменные окружения
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Копируем исходный код
COPY . .

# Запускаем скрипт
CMD ["python3", "main.py"]