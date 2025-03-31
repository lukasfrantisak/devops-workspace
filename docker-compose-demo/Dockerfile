FROM python:3.9-alpine

WORKDIR /app

COPY app.py .
COPY wait-for-postgres.sh /wait-for-postgres.sh

RUN pip install --no-cache-dir flask flask_sqlalchemy psycopg2-binary redis
RUN chmod +x /wait-for-postgres.sh

CMD ["/wait-for-postgres.sh"]