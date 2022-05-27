from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

title_validators = [DataRequired(), Length(max=100)]


class NewTaskForm(FlaskForm):
  title = StringField('New task:', validators=title_validators)
  submit = SubmitField('Add')


class EditTaskForm(FlaskForm):
  title = StringField('Task title:', validators=title_validators)
  submit = SubmitField('Save')
