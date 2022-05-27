from flask import url_for
from application import db
from application.models import Task
from tests import TestBase


class TestToggle(TestBase):
  # toggling a task between complete/incomplete works
  def test_toggle_complete(self):
    # add test task
    test_task = Task(title='Test task')
    db.session.add(test_task)
    db.session.commit()

    # toggle once to set is_complete to True
    self.client.post(url_for(f'toggle', id=test_task.id))
    assert Task.query.get(test_task.id).is_complete == True

    # toggle back to False
    self.client.post(url_for(f'toggle', id=test_task.id))
    assert Task.query.get(test_task.id).is_complete == False
