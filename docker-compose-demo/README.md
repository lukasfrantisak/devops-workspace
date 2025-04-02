# 🐳 Flask + Docker Compose Demo

Malý, ale silný projekt pro učení se Dockeru, vývoje ve Flasku a základů DevOps.  
Flask aplikace běží s PostgreSQL a Redisem díky Docker Compose.  
Součástí je i CI/CD pipeline přes GitHub Actions 🚀

---

## 🧠 Funkce

### 📋 Formulář pro návštěvníky
- Zápis jména → uložení do PostgreSQL
- Výpis všech návštěvníků

### ✅ TODO seznam
- Přidání úkolu s prioritou (nízká / střední / vysoká)
- Označení úkolu jako hotového
- Smazání úkolu
- Uložení do PostgreSQL

### 📊 Statistiky
- Počet návštěv (Redis)
- Počet hostů (PostgreSQL)

---

## 🛠 CI/CD

Projekt obsahuje CI workflow pomocí GitHub Actions:

```
📁 .github/workflows/
└── docker-ci.yml
```

CI provádí:
- ✅ Build Docker obrazu
- ✅ Ověření, že Flask app úspěšně startuje pomocí `test_app.py`

---

## 🚀 Spuštění projektu

1. Naklonuj repozitář:

```bash
git clone https://github.com/tvoje-username/tvuj-repozitar.git
cd docker-compose-demo
```

2. Spusť aplikaci:

```bash
docker compose up --build
```

3. Otevři v prohlížeči:

- [http://localhost:5001](http://localhost:5001) — hlavní stránka
- [http://localhost:5001/form](http://localhost:5001/form) — formulář
- [http://localhost:5001/tasks](http://localhost:5001/tasks) — TODO seznam
- [http://localhost:5001/stats](http://localhost:5001/stats) — statistiky

---

## 📁 Struktura projektu

```
docker-compose-demo/
├── app.py                 # Flask aplikace
├── test_app.py            # Test pro CI workflow
├── Dockerfile             # Definice Python kontejneru
├── docker-compose.yml     # Služby: web, postgres, redis
├── wait-for-postgres.sh   # Skript čekající na PostgreSQL
├── .github/
│   └── workflows/
│       └── docker-ci.yml  # CI/CD workflow
└── README.md              # Tento soubor
```

---

## 🧪 Plánovaný vývoj

- ✅ Formulář a zápis do DB
- ✅ TODO seznam s prioritami
- ✅ CI/CD workflow přes GitHub Actions
- ⏳ Možnost testování přes `pytest`
- 🌍 Deployment do cloudu (Render / Railway / Heroku)

---

## 📚 Technologie

- [🐍 Python 3.9 (Alpine)](https://hub.docker.com/_/python)
- [🔥 Flask](https://flask.palletsprojects.com/)
- [🐘 PostgreSQL](https://www.postgresql.org/)
- [⚡ Redis](https://redis.io/)
- [🐳 Docker + Compose](https://docs.docker.com/compose/)
- [🧪 GitHub Actions](https://docs.github.com/en/actions)

---

## ✨ Autor

👤 [@lukasfrantisak](https://github.com/lukasfrantisak)  
🎯 Cíl: stát se DevOps mistrem 💪  
