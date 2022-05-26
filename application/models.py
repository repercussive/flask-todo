from application import db

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  is_complete = db.Column(db.Boolean, default=False)