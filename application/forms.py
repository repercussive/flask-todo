from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
  title = StringField(
      "Task title:",
      validators=[DataRequired(), Length(max=100)]
  )
  submit = SubmitField()
