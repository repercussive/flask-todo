from flask import render_template
from application import app
from application.models import Task

@app.route('/')
def home():
  tasks = Task.query.all()
  return render_template('home.html', tasks=tasks)