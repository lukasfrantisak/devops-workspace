FROM python:3.9-alpine

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask psycopg2-binary

EXPOSE 5000

COPY wait-for-postgres.sh /wait-for-postgres.sh
CMD ["/wait-for-postgres.sh"]

