from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Task
from application.forms import TaskForm


@app.route('/')
def home():
  tasks = Task.query.all()
  form = TaskForm()
  return render_template('home.html', tasks=tasks, form=form, action='add')


@app.route('/add', methods=['POST'])
def add():
  new_task = Task(title=request.form['title'])
  db.session.add(new_task)
  db.session.commit()
  return redirect(url_for('home'))


@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
  task = Task.query.get(id)
  task.is_complete = not task.is_complete
  db.session.commit()
  return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
  task = Task.query.get(id)
  title = task.title
  form = TaskForm(title=title)

  if form.validate_on_submit():
    task.title = form.title.data
    db.session.commit()
    return redirect(url_for('home'))

  return render_template('edit.html', title=title, form=form, action=f'edit/{id}')
