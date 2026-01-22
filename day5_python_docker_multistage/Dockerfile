FROM python:3.10-slim AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir  -r requirements.txt --prefix=/install

FROM python:3.10-slim 

WORKDIR /app

COPY --from=build /install /usr/local/

COPY  . . 

EXPOSE 5000

CMD ["python", "app.py"]