from flask import Flask, request, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import redis

app = Flask(__name__)

# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres-db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Redis
redis_client = redis.Redis(host='redis-db', port=6379, decode_responses=True)

# SQLAlchemy model
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    count = redis_client.incr('visit_count')
    return f"Návštěva č. {count} (uloženo v Redis)"

@app.route('/form', methods=['GET', 'POST'])
def guest_form():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            guest = Guest(name=name)
            db.session.add(guest)
            db.session.commit()
            return redirect('/form')
    guests = Guest.query.order_by(Guest.timestamp.desc()).all()
    return render_template_string('''
        <h2>Zapiš se</h2>
        <form method="post">
            <input name="name" placeholder="Zadej jméno">
            <button type="submit">Odeslat</button>
        </form>
        <form method="post" action="/reset">
            <button type="submit">Resetovat počítadlo</button>
        </form>
        <h3>Seznam hostů:</h3>
        <ul>
        {% for g in guests %}
            <li>{{ g.name }} – {{ g.timestamp.strftime('%Y-%m-%d %H:%M:%S') }}</li>
        {% endfor %}
        </ul>
    ''', guests=guests)

@app.route('/dashboard')
def dashboard():
    count = redis_client.get('visit_count') or 0
    guest_count = Guest.query.count()
    return f'''
        <h2>📊 Dashboard</h2>
        <p>Počet návštěv (Redis): {count}</p>
        <p>Počet hostů (PostgreSQL): {guest_count}</p>
        <a href="/">← Zpět</a>
    '''

@app.route('/reset', methods=['POST'])
def reset_counter():
    redis_client.set('visit_count', 0)
    return redirect('/form')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)