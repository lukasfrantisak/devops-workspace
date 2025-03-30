from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="postgres-db",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="postgres"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Vytvoření tabulky, pokud neexistuje
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Zápis nové návštěvy
    cur.execute("INSERT INTO visits DEFAULT VALUES;")

    # Počet návštěv
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return f"Návštěva č. {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
