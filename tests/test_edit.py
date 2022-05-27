from flask import url_for
from application import db
from application.models import Task
from tests import TestBase


class TestEdit(TestBase):
  # (edit route, GET) gives a valid response
  def test_get(self):
    response = self.client.get(url_for('home'))
    assert response.status_code == 200

  # (edit route, POST) editing a task's title works
  def test_edit_task_title(self):
    # add test task
    test_task = Task(title='Test task')
    db.session.add(test_task)
    db.session.commit()

    # send request to change title
    self.client.post(
        url_for(f'edit', id=test_task.id),
        data={'title': 'A cool new title'}
    )

    # item in db is correctly updated
    assert Task.query.get(test_task.id).title == 'A cool new title'
