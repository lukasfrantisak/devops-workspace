import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host="postgres-db",
            database="mydatabase",
            user="postgres",
            password="mysecretpassword"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL!<br>Version: {version}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
