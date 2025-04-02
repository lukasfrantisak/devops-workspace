from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres-db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model pro návštěvy
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# Model pro úkoly
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# ⏳ Počkej, než bude PostgreSQL připraven
def wait_for_postgres():
    import psycopg2
    while True:
        try:
            conn = psycopg2.connect(
                host="postgres-db",
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

wait_for_postgres()
with app.app_context():
    db.create_all()

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)