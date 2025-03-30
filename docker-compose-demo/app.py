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
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        cur.execute("INSERT INTO visits DEFAULT VALUES;")
        conn.commit()

        cur.execute("SELECT COUNT(*) FROM visits;")
        count = cur.fetchone()[0]

        cur.close()
        conn.close()

        return f"Návštěva č. {count}"

    except Exception as e:
        print(f"❌ Chyba při zpracování požadavku: {e}")
        return f"❌ Chyba: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
