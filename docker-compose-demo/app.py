from flask import Flask, request, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import redis
import os

app = Flask(__name__)

# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres-db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Redis
redis_host = os.getenv("REDIS_HOST", "redis-db")
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# SQLAlchemy model
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), default='střední')  # nový řádek
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
        <form method="POST">
    <input type="text" name="description" placeholder="Nový úkol" required>
    <select name="priority">
        <option value="nízká">Nízká</option>
        <option value="střední" selected>Střední</option>
        <option value="vysoká">Vysoká</option>
    </select>
    <input type="submit" value="Přidat">
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

@app.route('/stats')
def stats():
    try:
        visits = redis_client.get('visit_count') or 0
        guests = Guest.query.count()
        return render_template_string('''
            <h2>📊 Statistiky</h2>
            <ul>
                <li>🔁 Počet návštěv (Redis): {{ visits }}</li>
                <li>👤 Počet hostů (PostgreSQL): {{ guests }}</li>
            </ul>
            <a href="/">🏠 Zpět na domovskou stránku</a>
        ''', visits=visits, guests=guests)
    except Exception as e:
        return f"❌ Chyba při načítání statistik: {e}"

# 📝 Výpis všech úkolů
@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        description = request.form.get('description')
        priority = request.form.get('priority', 'střední')
        if description:
            new_task = Task(description=description, priority=priority)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasks')

    tasks = Task.query.order_by(Task.timestamp.desc()).all()
    return render_template_string('''
        <h1>Seznam úkolů</h1>
        <form method="POST">
          <input type="text" name="description" placeholder="Nový úkol" required>
          <select name="priority">
            <option value="nízká">Nízká</option>
            <option value="střední" selected>Střední</option>
            <option value="vysoká">Vysoká</option>
          </select>
          <input type="submit" value="Přidat">
        </form>
        <ul>
        {% for task in tasks %}
            <li style="margin-bottom: 10px;">
                <form method="post" action="/toggle-task/{{ task.id }}" style="display:inline;">
                    <button type="submit">
                        {% if task.completed %}
                            ✅
                        {% else %}
                            ☐
                        {% endif %}
                    </button>
                </form>
                <span style="text-decoration: {% if task.completed %}line-through{% else %}none{% endif %};">
                    {{ task.description }}
                </span>
                <strong>[{{ task.priority|capitalize }}]</strong>
               <form method="post" action="/update-priority/{{ task.id }}" style="display:inline;">
    <select name="priority" onchange="this.form.submit()">
        <option value="nízká" {% if task.priority == 'nízká' %}selected{% endif %}>Nízká</option>
        <option value="střední" {% if task.priority == 'střední' %}selected{% endif %}>Střední</option>
        <option value="vysoká" {% if task.priority == 'vysoká' %}selected{% endif %}>Vysoká</option>
    </select>
</form>
            </li>
        {% endfor %}
        </ul>
        <a href="/">← Zpět na úvod</a>
    ''', tasks=tasks)

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

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
    return redirect('/tasks')

@app.route('/toggle-task/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/tasks')

@app.route('/delete-task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')

@app.route('/update-priority/<int:task_id>', methods=['POST'])
def update_priority(task_id):
    task = Task.query.get_or_404(task_id)
    new_priority = request.form.get('priority')
    if new_priority:
        task.priority = new_priority
        db.session.commit()
    return redirect('/tasks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)