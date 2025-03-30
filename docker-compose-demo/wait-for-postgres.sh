#!/bin/sh

# Čekej, dokud není PostgreSQL připravená
until nc -z postgres-db 5432; do
  echo "⏳ Čekám na PostgreSQL..."
  sleep 1
done

echo "✅ PostgreSQL je dostupná. Spouštím Flask..."
exec python app.py
