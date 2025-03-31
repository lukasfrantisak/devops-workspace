# 🐳 Docker Compose Demo – Flask + PostgreSQL + Redis

Tahle ukázková appka ti ukáže, jak spojit Flask aplikaci s PostgreSQL databází a Redisem pomocí Docker Compose. Navíc s jednoduchou CI pipeline přes GitHub Actions.

---

## 🚀 Funkce

- Flask aplikace se dvěma částmi:
  - 📋 Seznam úkolů (`/tasks`) s prioritami, označením hotovo a mazáním
  - 🧾 Návštěvní kniha (`/form`) + počítadlo návštěv uložené v Redis
- PostgreSQL pro ukládání dat
- Redis jako cache a návštěvní počítadlo
- CI/CD přes GitHub Actions (testy + build)

---

## 📁 Struktura projektu

\`\`\`
.
├── .github/workflows/
│   └── python-app.yml          # CI workflow (testy + build)
├── docker-compose-demo/
│   ├── app.py                  # Flask aplikace
│   ├── Dockerfile              # Docker image pro Flask appku
│   ├── docker-compose.yml      # Docker Compose config
│   ├── wait-for-postgres.sh    # Skript pro čekání na PostgreSQL
├── scripts/
│   └── pozdrav.sh              # Ukázkový shell skript
├── README.md
└── .gitignore
\`\`\`

---

## 🛠️ Spuštění lokálně

\`\`\`bash
# 1. Nakopni kontejnery
docker compose up --build

# 2. Aplikace běží na
http://localhost:5001
\`\`\`

---

## 🔎 Endpoints

- \`/\` – Redis: Počítadlo návštěv
- \`/form\` – Návštěvní kniha
- \`/tasks\` – Seznam úkolů (✅/🗑️/[🎯 Priorita])

---

## 🧪 Testování (GitHub Actions)

Testy se spouští automaticky při commitu:

- 🐍 Setup Python
- 📦 Instalace balíčků
- ✅ Basic test přes \`test.py\` (kontrola status kódu)

---

## 🧼 Úklid a konvence

- Shell skripty ve složce \`scripts/\`
- CI soubory v \`.github/workflows/\`
- \`.DS_Store\`, \`*.log\` a další bordel je ignorován přes \`.gitignore\`

---

## 🤓 Pro koho?

- Pro tebe, pokud se učíš Docker, Flask, CI/CD a chceš všechno propojit do smysluplné ukázky.

---

## ✨ TODO do budoucna

- [ ] Validace formulářů
- [ ] Pokročilejší Redis cache
- [ ] Přidat testy pro \`/form\` a \`/tasks\`

---

**Autor**: [@lukasfrantisak](https://github.com/lukasfrantisak)
