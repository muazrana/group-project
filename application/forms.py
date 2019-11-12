from flask_wtf import FlaskForm
from application.models import User
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
	name = StringField('Name',
		validators=[
		DataRequired(),
		Length(min=4, max=100)
		])

	submit = SubmitField('Post Content')

