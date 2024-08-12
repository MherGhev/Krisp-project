FROM python:3.10-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 8080

CMD ["python3", "app.py"]
