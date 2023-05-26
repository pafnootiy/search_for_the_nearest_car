
FROM python:3.8


ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

ENV POSTGRES_DB searching_app
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_HOST db
ENV POSTGRES_PORT 5432


CMD sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
