# Базовый образ
FROM ubuntu:22.04

# Установка зависимостей
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-17-jdk python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Определение JAVA_HOME с актуальным путем
RUN ln -s /usr/lib/jvm/java-17-openjdk-* /usr/lib/jvm/java-17-openjdk
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
ENV PATH=$JAVA_HOME/bin:$PATH

# Проверка установки
RUN java -version
RUN which java

# Установка зависимостей Python
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Копирование приложения
COPY . .

# Запуск приложения
CMD ["python3", "main.py"]