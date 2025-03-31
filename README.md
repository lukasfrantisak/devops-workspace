# 📝 Docker Compose Demo App

Tato aplikace je jednoduchý demo projekt běžící na Flasku, PostgreSQL a Redis. Umožňuje zaznamenávat návštěvy, přidávat hosty a spravovat úkoly s prioritou.

---

## 🚀 Spuštění projektu

```bash
docker compose up --build
```

Aplikace poběží na `http://localhost:5001`.

---

## 🧩 Použité technologie

- [x] **Flask** – jednoduchý Python web framework
- [x] **PostgreSQL** – relační databáze pro ukládání hostů a úkolů
- [x] **Redis** – in-memory store pro počítání návštěv
- [x] **Docker & Docker Compose** – kontejnerizace a orchestrace

---

## 🎯 Funkce aplikace

- Počítání návštěv (ukládáno do Redis)
- Formulář pro přidání jména do seznamu hostů (ukládáno do PostgreSQL)
- Seznam úkolů s možností:
  - Přidání
  - Označení jako hotové
  - Mazání
  - Nastavení priority (nízká, střední, vysoká)

---

## 📁 Struktura projektu

```
docker-compose-demo/
│
├── app.py                   # Hlavní Flask aplikace
├── Dockerfile               # Build instrukce pro backend
├── docker-compose.yml       # Kompozice služeb (Flask, PostgreSQL, Redis)
├── wait-for-postgres.sh     # Script pro čekání na databázi
├── README.md                # Dokumentace projektu
```

---

## 🧑‍💻 Autor

Projekt vytvořil **Lukáš Františák** v rámci praktického studia DevOps.
