# 🐍 Docker + Flask + PostgreSQL + Redis

Ukázkový projekt s jednoduchou Flask aplikací, která využívá:

- 🐳 Docker Compose pro orchestraci služeb
- 🐘 PostgreSQL pro ukládání dat
- ⚡ Redis jako cache a počítadlo návštěv
- 🧪 GitHub Actions pro CI

---

## 📂 Struktura složek

```
.
├── docker-compose-demo/        # Flask app + Docker setup
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── wait-for-postgres.sh
├── scripts/                    # Extra shell skripty
│   └── pozdrav.sh
├── .github/workflows/          # CI konfigurace
│   └── ci.yml
├── README.md                   # Tento soubor
└── .gitignore
```

---

## 🚀 Spuštění projektu

```bash
cd docker-compose-demo
docker compose up --build
```

🧭 Aplikace poběží na: [http://localhost:5001](http://localhost:5001)
