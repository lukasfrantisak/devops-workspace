# 🐳 Flask + Redis + PostgreSQL + Docker Compose

Tento projekt je první praktickou ukázkou propojení několika základních technologií pomocí Docker Compose.  
Obsahuje jednoduchou Flask aplikaci, která ukládá data do PostgreSQL, využívá Redis pro sledování návštěv a je připravena pro CI/CD přes GitHub Actions.

## ⚙️ Použité technologie

- [Flask](https://flask.palletsprojects.com/) – jednoduchý webový framework v Pythonu
- [PostgreSQL](https://www.postgresql.org/) – relační databáze
- [Redis](https://redis.io/) – key-value store pro cache a počítadlo návštěv
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM pro práci s databází
- [Docker Compose](https://docs.docker.com/compose/) – správa více služeb v kontejnerech
- [GitHub Actions](https://docs.github.com/actions) – CI/CD pipeline (build + test)

## 🚀 Co aplikace umí

- 📝 Umožňuje zadat a spravovat úkoly (seznam úkolů s prioritou)
- ✅ Úkoly lze označovat jako hotové, mazat a filtrovat podle priority
- 👤 Zaznamenává jména "hostů" přes jednoduchý formulář
- 🔁 Sleduje počet návštěv pomocí Redis
- 📊 Zobrazuje základní statistiky

## 🧠 Proč to vzniklo?

Celý projekt vznikl jako součást mé cesty k pochopení DevOps a moderního vývoje.  
Krok za krokem se učím pracovat s Dockerem, databázemi, CI/CD a verzováním pomocí Git a GitHubu.

## 🛠️ Jak spustit lokálně

```bash
git clone https://github.com/TVOJEJMENO/docker-compose-demo.git
cd docker-compose-demo
docker compose up --build
```

Aplikace poběží na [http://localhost:5001](http://localhost:5001)

## ✅ CI/CD s GitHub Actions

Každý push na `main` spustí build + základní test v GitHub Actions.

## 🧹 TODO

- [ ] Přidat filtrování úkolů podle priority
- [ ] Dodělat jednoduché testy
- [ ] Deployment (např. přes Fly.io nebo Railway)

---

## ✍️ Autor

Projekt vytvářím jako součást své vlastní cesty ke kariéře v DevOps.  
Více o mně najdeš na [frantisak.cz](https://frantisak.cz) nebo na [Instagramu](https://instagram.com/lukas.frantisak).