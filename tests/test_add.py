from flask import url_for
from application.models import Task
from tests import TestBase


class TestAdd(TestBase):
  # (add route, POST) adding a task via POST works
  def test_add_task(self):
    self.client.post(
        url_for('add'),
        data=dict(title='New task')
    )
    new_task = Task.query.first()
    assert new_task.title == 'New task'
