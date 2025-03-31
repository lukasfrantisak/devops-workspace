# DevOps Playground – Flask + PostgreSQL + Redis (Docker Compose)

Tahle ukázková appka vznikla jako součást mé cesty k pochopení DevOps světa. Krok za krokem tu rozvíjím jednoduchý Flask projekt, který běží v Docker Compose a spojuje tři služby:

- 🐍 Flask – samotná webová aplikace  
- 🐘 PostgreSQL – relační databáze  
- 🚀 Redis – rychlá cache (např. pro počítadlo návštěv)

---

## 🔧 Co to umí

- 📋 Správa úkolů s prioritou, stavem „hotovo“ a mazáním  
- 📝 Formulář pro zadávání jmen návštěvníků  
- 📊 Statistiky a návštěvnost sledovaná přes Redis  
- 🔁 CI/CD pipeline přes GitHub Actions  
- 🐳 Všechno běží v Dockeru, odděleně a elegantně

---

## 📂 Struktura složek

\`\`\`
.
├── docker-compose-demo/        # Flask app + Docker setup
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── wait-for-postgres.sh
├── scripts/                    # Extra shell skripty
│   └── pozdrav.sh
├── .github/workflows/          # CI konfigurace
│   └── python-app.yml
├── README.md                   # Tento soubor
└── .gitignore
\`\`\`

---

## 🚀 Spuštění projektu

\`\`\`bash
cd docker-compose-demo
docker compose up --build
\`\`\`

> Aplikace poběží na: [http://localhost:5001](http://localhost:5001)

---

## 🛠 Work in Progress

Tohle je živý playground – zkouším, ladím, učím se.  
Není to finální produkt, ale otevřený sandbox pro učení se DevOps v praxi.

---

## 👨‍💻 Autor

Projekt vede: **[@lukasfrantisak](https://github.com/lukasfrantisak)**  
Pokud máš feedback nebo tip na zlepšení, klidně napiš ✌️
