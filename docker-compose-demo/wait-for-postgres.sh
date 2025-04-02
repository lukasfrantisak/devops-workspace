#!/bin/sh
# Počkáme, než PostgreSQL začne naslouchat na TCP portu
echo "⏳ Čekám na PostgreSQL..."
while ! nc -z postgres-db 5432; do
  sleep 0.5
done
echo "✅ PostgreSQL je dostupná. Spouštím Flask..."
exec "$@"