from flask import url_for
from application import db
from application.models import Task
from tests import TestBase


class TestApp(TestBase):
  # (home route, GET) gives a valid response on GET
  def test_get_home(self):
    response = self.client.get(url_for('home'))
    self.assert200(response)

  # (home route, GET) the tasks in the db are sent in the response
  def test_get_tasks(self):
    test_task = Task(title='A cool task')
    db.session.add(test_task)
    db.session.commit()

    response = self.client.get(url_for('home'))
    self.assertIn(b'A cool task', response.data)
