from flask import url_for
from application import db
from application.models import Task
from tests import TestBase


class TestHome(TestBase):
  # (home route, GET) gives a valid response on GET
  def test_get(self):
    response = self.client.get(url_for('home'))
    assert response.status_code == 200

  # (home route, GET) the tasks in the db are sent in the response
  def test_tasks_received(self):
    test_task = Task(title='A cool task')
    db.session.add(test_task)
    db.session.commit()

    response = self.client.get(url_for('home'))
    assert b'A cool task' in response.data
