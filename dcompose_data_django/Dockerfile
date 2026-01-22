FROM python:3.11-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install  -y  \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt 

FROM python:3.11-slim

WORKDIR /app
COPY --from=build /install /urs/local

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]