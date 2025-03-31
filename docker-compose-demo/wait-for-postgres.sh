#!/bin/sh
echo "⏳ Čekám na PostgreSQL..."
while ! nc -z postgres-db 5432; do
  sleep 0.1
done
echo "✅ PostgreSQL je dostupná. Spouštím Flask..."
exec python app.py