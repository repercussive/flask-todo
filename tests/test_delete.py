from flask import url_for
from application import db
from application.models import Task
from tests import TestBase


class TestDelete(TestBase):
  # (delete route, POST) deleting a task works
  def test_delete_task(self):
    # add test task
    test_task = Task(title='Test task')
    db.session.add(test_task)
    db.session.commit()

    # after the delete request is sent, the task no longer exists
    self.client.post(url_for(f'delete', id=test_task.id))
    assert Task.query.get(test_task.id) is None
