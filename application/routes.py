from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Task
from application.forms import TaskForm


@app.route('/')
def home():
  tasks = Task.query.all()
  form = TaskForm()
  return render_template('home.html', tasks=tasks, form=form)


@app.route('/add', methods=['POST'])
def add():
  new_task = Task(title=request.form['title'])
  db.session.add(new_task)
  db.session.commit()
  return redirect(url_for('home'))
