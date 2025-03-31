# Flask + PostgreSQL + Redis (Docker Compose)

This is a simple demo application using Flask, PostgreSQL, and Redis connected via Docker Compose.

## 🇺🇸 English

### 💡 What it does

- Counts visits using **Redis**
- Stores guest names with timestamps in **PostgreSQL**
- Displays a dashboard with guest list and a form

### 🧱 Stack

- **Flask** (Python)
- **PostgreSQL** (via SQLAlchemy)
- **Redis**
- **Docker Compose**

### ▶️ How to run

```bash
# Clone the repo
git clone https://github.com/lukasfrantisak/devops-workspace.git
cd devops-workspace/docker-compose-demo

# Build and run
docker compose up --build
```

Open your browser:

- [http://localhost:5001/](http://localhost:5001/) – Visit counter
- [http://localhost:5001/form](http://localhost:5001/form) – Guest form
- [http://localhost:5001/dashboard](http://localhost:5001/dashboard) – Guest dashboard

### 🧹 Reset database (optional)

```bash
docker compose down -v
```

---

## 🇨🇿 Čeština

### 💡 Co to dělá

- Počítá návštěvy pomocí **Redis**
- Ukládá jména a čas přidání do **PostgreSQL**
- Zobrazuje dashboard se seznamem a formulářem

### 🧱 Použité technologie

- **Flask** (Python)
- **PostgreSQL** (přes SQLAlchemy)
- **Redis**
- **Docker Compose**

### ▶️ Jak spustit

```bash
# Klonování repozitáře
git clone https://github.com/lukasfrantisak/devops-workspace.git
cd devops-workspace/docker-compose-demo

# Build a spuštění
docker compose up --build
```

Otevři prohlížeč:

- [http://localhost:5001/](http://localhost:5001/) – Počítadlo návštěv
- [http://localhost:5001/form](http://localhost:5001/form) – Formulář
- [http://localhost:5001/dashboard](http://localhost:5001/dashboard) – Dashboard se seznamem

### 🧹 Reset databáze (volitelně)

```bash
docker compose down -v
```
