
# 🐳 Flask + Docker Compose demo

Jednoduchý projekt, kde běží Flask aplikace s PostgreSQL a Redisem pomocí Docker Compose. Cílem je naučit se základy vývoje, práce s kontejnery a připravit prostředí pro CI/CD.

---

## 🧠 Co to umí

- 📋 **Formulář pro návštěvníky**
  - Zápis jména a uložení do PostgreSQL
  - Výpis všech návštěvníků
- 📝 **TODO seznam**
  - Přidání úkolu s prioritou (nízká, střední, vysoká)
  - Označení úkolu jako hotového
  - Smazání úkolu
  - Uložení do PostgreSQL
- 📊 **Statistiky**
  - Počet návštěv uložený v Redis
  - Počet hostů v databázi

---

## 🚀 Spuštění projektu

1. Naklonuj repozitář:

```bash
git clone https://github.com/tvoje-username/tvuj-repozitar.git
cd tvuj-repozitar
```

2. Spusť aplikaci:

```bash
docker compose up --build
```

3. Otevři v prohlížeči:

- http://localhost:5001 — hlavní stránka
- http://localhost:5001/form — formulář pro návštěvníky
- http://localhost:5001/tasks — TODO seznam
- http://localhost:5001/stats — statistiky

---

## 🧱 Struktura projektu

```
📁 docker-compose-demo
├── app.py                 # Flask aplikace
├── Dockerfile             # Build kontejneru s Pythonem
├── docker-compose.yml     # Definice služeb (Flask, Redis, PostgreSQL)
├── wait-for-postgres.sh   # Skript čekající na PostgreSQL
└── README.md              # Tento soubor
```

---

## ✍️ Co plánujeme dál

- ✅ Přidání priority do úkolů
- ✅ Funkce označit jako hotovo + mazání
- 🔄 CI/CD workflow přes GitHub Actions
- 🌍 Deployment aplikace do cloudu (Render / Railway / Heroku / ...)

---

## 📚 Využité technologie

- [Python 3.9 (Alpine)](https://hub.docker.com/_/python)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ✨ Autor

👤 [@lukasfrantisak](https://github.com/lukasfrantisak)  
🎯 Cíl: stát se DevOps mistrem 💪
