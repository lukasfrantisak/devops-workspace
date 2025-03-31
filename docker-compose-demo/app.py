from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from datetime import datetime
import os

app = Flask(__name__)

# OPRAVA: správné jméno hostitele pro PostgreSQL v rámci GitHub Actions
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")  # <- změna z "postgres-db"
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")  # <- GitHub Actions alias
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default="střední")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def index():
    count = redis.incr("hits")
    return f"Tato stránka byla navštívena {count}krát."

@app.route("/visitors", methods=["GET", "POST"])
def visitors():
    if request.method == "POST":
        name = request.form["name"]
        visitor = Visitor(name=name)
        db.session.add(visitor)
        db.session.commit()
        return redirect(url_for("visitors"))
    all_visitors = Visitor.query.order_by(Visitor.timestamp.desc()).all()
    return render_template("visitors.html", visitors=all_visitors)

@app.route("/tasks", methods=["GET", "POST"])
def task_list():
    if request.method == "POST":
        description = request.form["description"]
        priority = request.form["priority"]
        task = Task(description=description, priority=priority)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("task_list"))
    tasks = Task.query.order_by(Task.timestamp.desc()).all()
    return render_template("tasks.html", tasks=tasks)

@app.route("/tasks/<int:task_id>/done", methods=["POST"])
def mark_done(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
    return redirect(url_for("task_list"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("task_list"))