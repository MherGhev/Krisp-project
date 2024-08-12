FROM python:3.10-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask requests redis cachetools

EXPOSE 8081

CMD ["python3", "app.py"]
