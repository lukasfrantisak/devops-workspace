from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)

# 🔧 Dynamické připojení podle prostředí
DB_HOST = 'postgres-db' if not app.testing else 'localhost'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:postgres@{DB_HOST}:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

def wait_for_postgres():
    import psycopg2
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database="postgres",
                user="postgres",
                password="postgres"
            )
            conn.close()
            print("✅ PostgreSQL je dostupná. Spouštím Flask...")
            break
        except:
            print("⏳ Čekám na PostgreSQL...")
            time.sleep(1)

@app.route('/')
def index():
    return "<h1><b>Flask + Docker is alive 🚀</b></h1>"

@app.route('/visits')
def visits():
    visitor = Visitor()
    db.session.add(visitor)
    db.session.commit()
    count = Visitor.query.count()
    return f"<h1>Počet návštěv: {count}</h1>"

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        desc = request.form.get('description')
        if desc:
            new_task = Task(description=desc)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('tasks'))

    tasks = Task.query.all()
    return render_template_string('''
        <h1>Seznam úkolů 📝</h1>
        <form method="post">
            <input name="description" placeholder="Zadej nový úkol">
            <button type="submit">Přidat</button>
        </form>
        <ul>
        {% for task in tasks %}
            <li>{{ task.description }}</li>
        {% endfor %}
        </ul>
    ''', tasks=tasks)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"<h2>Díky, {name}!</h2>"

    return render_template_string('''
        <h2>Zadej své jméno</h2>
        <form method="POST">
            <input name="name" placeholder="Tvé jméno">
            <button type="submit">Odeslat</button>
        </form>
    ''')

if __name__ == '__main__':
    wait_for_postgres()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)