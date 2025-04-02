FROM python:3.9-alpine

RUN apk add --no-cache netcat-openbsd gcc musl-dev libpq

WORKDIR /app

COPY app.py .
COPY wait-for-postgres.sh /wait-for-postgres.sh

RUN chmod +x /wait-for-postgres.sh

RUN pip install --no-cache-dir flask flask_sqlalchemy psycopg2-binary

CMD ["/wait-for-postgres.sh", "python", "app.py"]